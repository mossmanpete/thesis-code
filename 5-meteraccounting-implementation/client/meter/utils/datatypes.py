class Method:
    URNS_CSV = 'getCsvForUrns'
    CURRENT_CSV  = 'getCurrentValuesCsv'
    CURRENT_JSON = 'getCurrentValuesJson'
    GET_VALUES_AT_TIME_JSON = 'getValuesAtTimeJson'

class Timemode:
    TIMESTAMP = 'timestamp'
    DATETIME = 'timeanddate'
    LOCAL = 'localtime'

class Extra:
    CHANGE_OF_VALUE = 'changeOfValue'
    EXCEL = 'excel'
    INTERVAL = 'interval'

class NumberFormat:
    DE = 'de'

class Coefficients:
    F1 = 3.3
    F2 = 6060.0 / 44020
    F3 = 6020.0 / 44020
    F5 = 608.0 / 3212
    F6 = 1280.0 / 44020
    F7 = 210.0 / 4986
    F8 = 210.0 / 1180
    F9 = 125.0 / 4986
    F10 = 135.0 / 1784
    F11 = 87.0 / 3209
    F12 = 1500.0 / 44020
    F13 = 35.0 / 223
    F14 = 69.0 / 2807
    F15 = 349.0 / 2807
    F16 = 127.0 / 223
    F17 = 751.0 / 2807
    F18 = 43.0 / 223
    F19 = 191.0 / 2807
    F20 = 532.0 / 3209
    F21 = 12000.0 / 44020
    F22 = 662.0 / 3209
    F23 = 7000.0 / 44020
    F24 = 1730.0 / 3209
    F25 = 8800.0 / 44020
    F26 = 57.0 / 2807
    F27 = 18.0 / 223
    F28 = 96.0 / 3212
    F29 = 60.0 / 2278
    F30 = 36.0 / 456
    F31 = 210.0 / 456
    F32 = 210.0 / 3212
    F33 = 360.0 / 2278
    F34 = 360.0 / 3212
    F35 = 86.0 / 2807
    F36 = 112.0 / 456
    F37 = 337.0 / 4986
    F38 = 337.0 / 1180
    F39 = 423.0 / 4986
    F40 = 423.0 / 1180
    F41 = 1359.0 / 2278
    F42 = 1359.0 / 3212
    F47 = 35.0 / 4986
    F48 = 35.0 / 1006
    F49 = 331.0 / 4986
    F50 = 331.0 / 1784
    F51 = 360.0 / 4986
    F52 = 72.0 / 1784
    F53 = 30.0 / 4986
    F54 = 30.0 / 1006
    F55 = 240.0 / 4986
    F56 = 240.0 / 1784
    F57 = 80.0 / 2807
    F58 = 672.0 / 805
    F59 = 133.0 / 805
    F61 = 117.0 / 1784
    F62 = 469.0 / 744
    F63 = 275.0 / 744
    F64 = 204.0 / 370
    F65 = 86.0 / 370
    F66 = 80.0 / 370
    F67 = 1076.0 / 2807
    F68 = 2146.0 / 4986
    F69 = 235.0 / 1180
    F70 = 360.0 / 1006
    F71 = 1360.0 / 1784
    F72 = 199.0 / 3209
    F73 = 506.0 / 2278
    F74 = 506.0 / 3212
    F75 = 105.0 / 456
    F76 = 105.0 / 3212

class Time:
    NOW            = "NOW"
    CURRENT_YEAR   = "CURRENT_YEAR"
    CURRENT_MONTH  = "CURRENT_MONTH"
    CURRENT_WEEK   = "CURRENT_WEEK"
    CURRENT_DAY    = "CURRENT_DAY"
    NEXT_YEAR      = "NEXT_YEAR"
    NEXT_MONTH     = "NEXT_MONTH"
    NEXT_WEEK      = "NEXT_WEEK"
    NEXT_DAY       = "NEXT_DAY"
    PREVIOUS_YEAR  = "PREVIOUS_YEAR"
    PREVIOUS_MONTH = "PREVIOUS_MONTH"
    PREVIOUS_WEEK  = "PREVIOUS_WEEK"
    PREVIOUS_DAY   = "PREVIOUS_DAY"
    START_OF_YEAR  = "START_OF_YEAR"
    START_OF_MONTH = "START_OF_MONTH"
    START_OF_WEEK  = "START_OF_WEEK"
    START_OF_DAY   = "START_OF_DAY"
    RY_Month_1  = "RY_Month(1)"
    RY_Month_2  = "RY_Month(2)"
    RY_Month_3  = "RY_Month(3)"
    RY_Month_4  = "RY_Month(4)"
    RY_Month_5  = "RY_Month(5)"
    RY_Month_6  = "RY_Month(6)"
    RY_Month_7  = "RY_Month(7)"
    RY_Month_8  = "RY_Month(8)"
    RY_Month_9  = "RY_Month(9)"
    RY_Month_10 = "RY_Month(10)"
    RY_Month_11 = "RY_Month(11)"
    RY_Month_12 = "RY_Month(12)"
    RY_Month_13 = "RY_Month(13)"
    RY_Month_14 = "RY_Month(14)"
    RY_Month_15 = "RY_Month(15)"
    RY_Month_16 = "RY_Month(16)"
    RY_Month_17 = "RY_Month(17)"
    RY_Month_18 = "RY_Month(18)"
    RY_Month_19 = "RY_Month(19)"
    RY_Month_20 = "RY_Month(20)"
    RY_Month_21 = "RY_Month(21)"
    RY_Month_22 = "RY_Month(22)"
    RY_Month_23 = "RY_Month(23)"
    RY_Month_24 = "RY_Month(24)"
    RY_Month_25 = "RY_Month(25)"

class Operator(object):
    ACTIVATE = 'activateMeter'
    DEACTIVATE = 'deactivateMeter'


class MeterNames(object):
    ELT01 = "H2.Z64.W"
    ELT02 = "H2.Z65.W"
    ELT03 = "H3.Z71.W"
    ELT04 = "H2.Z66.W"
    ELT05 = "H2.Z67.W"
    ELT06 = "H3.Z46.W"
    ELT07 = "H3.Z71.W"
    ELT08 = "H3.Z43.W"
    ELT09 = "H3.Z44.W"
    ELT10 = "H3.Z40.W"
    ELT11 = "H3.Z45.W"
    ELT12 = "H3.Z42.W"
    ELT13 = "H3.Z41.W"
    ELT13 = "H4.Z51.W"
    ELT14 = "H4.Z50.W"
    ELT15 = "H2.T.Z31.W"
    ELT16 = "H1.Z11.W"
    ELT17 = "H1.Z12.W"
    ELT18 = "H1.Z16.W"
    ELT19 = "H1.Z24.W"
    ELT20 = "H1.Z25.W"
    ELT21 = "H2.T.Z34.W"
    ELT22 = "H2.Z61.W"
    ELT23 = "H2.Z62.W"
    ELT24 = "H2.Z63.W"
    ELT25 = "H2.Z68.W"
    ELT26 = "H2.Z69.W"
    ELT27 = "H2.Z70.W"
    ELT28 = "H2.T.Z33.W"
    ELT29 = "H1.Z26.W"
    ELT30 = "H1.Z27.W"
    ELT31 = "H1.Z10.W"
    ELT32 = "H1.Z18.W"
    ELT33 = "H1.Z21.W"
    ELT34 = "H1.Z22.W"
    ELT35 = "H1.Z13.W"
    ELT36 = "H1.Z14.W"
    # ELT37 = "V.Z81.Wtot"
    ELT37 = "V.Z81.W"
    # ELT38 = "V.Z82.Wtot"
    ELT38 = "V.Z82.W"
    # ELT39 = "H1.Z19.Wtot"
    ELT39 = "H1.Z19.W"
    ELT40 = "H1.Z20.W"
    # ELT41 = "H1.Z23.Wtot"
    ELT41 = "H1.Z23.W"
    ELT42 = "H2.T.Z32.W"
    ELT43 = "H2.T.Z30.W"
    ELT44 = "H2.Z35.W"
    ELT45 = "H2.Z36.W"
    ELT46 = "H1.Z17.W"
    KMZ1  = "V.K22.W"
    KMZ2  = "V.K21.W"
    KMZ3  = "H2.K21.W"
    KMZ4  = "H1.K11.W"
    KMZ5  = "H1.K15.W"
    KMZ6  = "H1.K12.W"
    KMZ7  = "H1.K14.W"
    VM01  = 'VM01'
    VM02  = 'VM02'
    VM03  = 'VM03'
    VM04  = 'VM04'
    VM05  = 'VM05'
    VM06  = 'VM06'
    VM07  = 'VM07'
    VM08  = 'VM08'
    VM09  = 'VM09' 
    VM10  = 'VM10'
    VM11  = 'VM11'
    VM12  = 'VM12'
    VM13  = 'VM13'
    VM14  = 'VM14'
    VM15  = 'VM15'
    VM16  = 'VM16'
    VM17  = 'VM17'
    VM18  = 'VM18'
    VM19  = 'VM19'
    VM20  = 'VM20'
    VM21  = 'VM21'
    VM22  = 'VM22'
    VM23  = 'VM23'
    VM24  = 'VM24'
    VM25  = 'VM25'
    VM26  = 'VM26'
    VM27  = 'VM27'
    VM28  = 'VM28'
    VM29  = 'VM29'
    VM30  = 'VM30'
    VM31  = 'VM31'
    VM32  = 'VM32'
    VM33  = 'VM33'
    VM34  = 'VM34'
    VM35  = 'VM35'
    VM36  = 'VM36'
    VM37  = 'VM37'
    VM38  = 'VM38'
    VM39  = 'VM39'
    VM40  = 'VM40'
    VM41  = 'VM41'
    VM42  = 'VM42'
    VM43  = 'VM43'
    VM44  = 'VM44'


class Permissions:
    RegistryOperator = 1
    MeterOperator    = 2
    AccountingOperator = 3
    Accountant         = 4


