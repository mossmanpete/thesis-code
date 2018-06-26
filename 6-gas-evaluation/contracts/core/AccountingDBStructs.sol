pragma solidity ^0.4.21;

/**
 * @title AccountingDb
 * @dev Handles all accounting logic for departments
 */

contract AccountingDBStructs  {

    /* Events */
    event Activated(bytes32 indexed department);
    event Deactivated(bytes32 indexed department);
    event Forwarded(bytes32 indexed from, bytes32 indexed to, uint80 amount);
    event Cleared(bytes32 indexed department, uint80 amount);

    /* Storage */
    struct Department {
        bool active;
        uint8 headcount;
        uint80 power;
        uint80 delegatedPower;
        uint80 clearedPower;
        bytes32[] delegates; // Departments to delegate to
        bytes32[] subdepartments; // Departments to get readings from, used for top level departments such as HREG or for Admin_HRE
        bytes8[] virtualmeters; // IDs of virtual meters { VM01- VM44} Should be bytes8 because that's how we define it in MeterDB
    }

    mapping (bytes32 => Department) departments; // arrays of delegate/departments/virtual meters


    /* Public functions */

    /// @dev Called by an operator to activate multiple departments in storage
    /// @param departmentIDs array of Department IDs
    function activateDepartments(bytes32[] departmentIDs) external {
        uint length = departmentIDs.length;

        for (uint i=0; i<length; i++) {
            activateDepartment(departmentIDs[i]);
        }

    }

    /// @dev Called by an operator to activate a department in storage
    /// @param departmentID the ID of the department
    function activateDepartment(bytes32 departmentID) public { 
        departments[departmentID].active = true;
        emit Activated(departmentID);
    }

    /// @dev Called by an operator to deactivate a department in storage
    /// @param departmentID the ID of the department
    function deactivateDepartment(bytes32 departmentID) external  { 
        delete departments[departmentID];

        emit Deactivated(departmentID);
    }

    /// @dev Called by an operator to set the delegates for a department
    /// @param departmentID the ID of the department
    /// @param delegates array with the IDs of the delegates
    function setDelegates(bytes32 departmentID, bytes32[] delegates) external  {
        departments[departmentID].delegates = delegates;
    }

    /// @dev Called by an operator to set the virtualmeters for a department
    /// @param departmentID the ID of the department
    /// @param virtualmeters array with the IDs of the virtualmeters
    function setVirtualMeters(bytes32 departmentID, bytes8[] virtualmeters) external  {
        departments[departmentID].virtualmeters = virtualmeters;
    }

    /// @dev Called by an operator to set the subdepartments for a department
    /// @param departmentID the ID of the department
    /// @param subdepartments array with the IDs of the subdepartments
    function setSubDepartments(bytes32 departmentID, bytes32[] subdepartments) external  {
        departments[departmentID].subdepartments = subdepartments;
    }

    /// @dev Called by an operator to set the headcount for a department
    /// @param departmentID the ID of the department
    /// @param headcount the headcount PERCENTAGE of that department
    function setHeadcount(bytes32 departmentID, uint8 headcount) external  {
        departments[departmentID].headcount = headcount;
    }


    /// @dev Given a departmentID fetch the delegates/subdepartments/virtualmeters
    /// @param departmentID the ID of the department
    function getAccountingData(bytes32 departmentID) external view returns (bytes32[], bytes32[], bytes8[]) {
        return (
           departments[departmentID].delegates,
           departments[departmentID].subdepartments,
           departments[departmentID].virtualmeters
        );
    }

    /// @dev Given a departmentID fetch if the department is active, its ehadcount and its power, delegated power and cleared power
    /// @param departmentID the ID of the department
    function getDepartmentData(bytes32 departmentID) 
    external 
    view 
    returns (bool, uint8, uint80, uint80, uint80) 
    {

        Department memory department = departments[departmentID];
        return (
            department.active,
            department.headcount,
            department.power,
            department.delegatedPower,
            department.clearedPower
        );
    }

    /// @dev Called by an accountant to forward the consumption of a department to two other departments, split in X% and (100-X)%
    /// @param from the ID of the sending department
    /// @param pct the *percentage* that will get forwarded to the first delegate. The rest gets sent to the second delegate.
    function fixedSplit(bytes32 from, uint8 pct) external  {
        bytes32[] memory to = departments[from].delegates; // the receiving departments are the delegates
        require(to.length == 2);
        require(pct >=0 && pct <= 100);

        uint80 power_for_delegation = departments[from].power;

        // delegate to the 2 receiving departments
        departments[to[0]].delegatedPower += power_for_delegation * pct / 100;

        emit Forwarded(
            from, 
            to[0], 
            power_for_delegation * pct / 100
        );

        departments[to[1]].delegatedPower += power_for_delegation * (100-pct) / 100;

        emit Forwarded(
            from, 
            to[1], 
            power_for_delegation * (100-pct) / 100
        );

        // Clear
        clearDepartment(from, power_for_delegation);
    }



    /// @dev Called by an accountant to forward the consumption of a department based on its delegates' headcounts. 
    /// @param from the ID of the sending department
    function headcountSplit(bytes32 from) external  {

        Department memory receiver;
        bytes32[] memory to = departments[from].delegates;

        uint80 power_for_delegation = departments[from].power;
        uint80 power;
        uint8 headcount;
        uint length = to.length;


        for (uint i = 0 ; i < length ; i++) {
            receiver = departments[to[i]]; // 
            headcount = receiver.headcount;

            power = power_for_delegation * headcount / 100;
            receiver.delegatedPower += power;

            // and store it back
            departments[to[i]] = receiver;

            emit Forwarded(from, to[i], power);
        }

        clearDepartment(from, power_for_delegation);
    }

    /// @dev Called by an accountant to bill a department. If a department has been cleared int he past, the cleared amount is not billed again to prevent double-billing
    /// @param departmentID the department to be billed
    /// @param power the power consumption to be billed
    function billPower(bytes32 departmentID, uint80 power) external {
        Department memory department = departments[departmentID];
        uint80 cleared = department.clearedPower;

        // Since meters always ping their latest value
        // only bill power that has not been cleared yet
        // by definition cleared < power
        department.power = power - cleared;
        departments[departmentID] = department;
    }

    /// @dev Called by an accountant to clear a department. It increases the amount of power that has been cleared, and resets the deparment's power.
    /// @param departmentID the department to be cleared
    /// @param cleared the power consumption to be cleared
    function clearDepartment(bytes32 departmentID, uint80 cleared) public  { // an accountant can call that too
        Department memory department = departments[departmentID];
        department.clearedPower += cleared;
        department.power = 0;

        departments[departmentID] = department;

        emit Cleared(departmentID, cleared);
    }
}
