"""
Test Results for discrete models from Stata
"""

import numpy as np

#### Discrete Model Tests ####
# Note that there is a slight refactor of the classes, so that one dataset
# might be used for more than one model

class Anes():
    def __init__(self):
        """
        Results are from Stata 11 (checked vs R nnet package).
        """
        self.nobs = 944

    def mnlogit_basezero(self):
        params = [-.01153598, .29771435, -.024945, .08249144, .00519655,
                -.37340167, -.08875065, .39166864, -.02289784, .18104276,
                .04787398, -2.2509132, -.1059667, .57345051, -.01485121,
                -.00715242, .05757516, -3.6655835, -.0915567, 1.2787718,
                -.00868135, .19982796, .08449838, -7.6138431, -.0932846,
                1.3469616, -.01790407, .21693885, .08095841, -7.0604782,
                -.14088069, 2.0700801, -.00943265, .3219257, .10889408,
                -12.105751]
        self.params = np.reshape(params, (6,-1))
        bse = [.0342823657, .093626795, .0065248584, .0735865799,
                .0176336937, .6298376313, .0391615553, .1082386919,
                .0079144618, .0852893563, .0222809297, .7631899491,
                .0570382292, .1585481337, .0113313133, .1262913234,
                .0336142088, 1.156541492, .0437902764, .1288965854,
                .0084187486, .0941250559, .0261963632, .9575809602,
                .0393516553, .1171860107, .0076110152, .0850070091,
                .0229760791, .8443638283, .042138047, .1434089089,
                .0081338625, .0910979921, .025300888, 1.059954821]
        self.bse = np.reshape(bse, (6,-1))
        self.cov_params = None
        self.llf = -1461.922747312
        self.llnull = -1750.34670999
        self.llr = 576.8479253554
        self.llr_pvalue = 1.8223179e-102
        self.prsquared = .1647810465387
        self.df_model = 30
        self.df_resid = 944 - 36
        self.J = 7
        self.K = 6
        self.aic = 2995.84549462
        self.bic = 3170.45003661
        z =  [-.3364988051, 3.179798597,  -3.823070772, 1.121012042,
            .2946945327, -.5928538661, -2.266269864, 3.618564069,
            -2.893164162, 2.122688754, 2.148652536, -2.949348555,
            -1.857818873, 3.616885888, -1.310634214, -.0566342868,
            1.712822091, -3.169435381, -2.090799808, 9.920912816,
            -1.031191864, 2.123004903, 3.225576554, -7.951122047,
            -2.370538224, 11.49421878, -2.352389066, 2.552011323,
            3.523595639, -8.361890935, -3.34331327, 14.43480847,
            -1.159676452, 3.533839715, 4.303962885, -11.42100649]
        self.z = np.reshape(z, (6,-1))
        pvalues = [0.7364947525, 0.0014737744, 0.0001317999, 0.2622827367,
            0.7682272401, 0.5532789548, 0.0234348654, 0.0002962422,
            0.0038138191, 0.0337799420, 0.0316619538, 0.0031844460,
            0.0631947400, 0.0002981687, 0.1899813744, 0.9548365214,
            0.0867452747, 0.0015273542, 0.0365460134, 3.37654e-23,
            0.3024508550, 0.0337534410, 0.0012571921, 1.84830e-15,
            0.0177622072, 1.41051e-30, 0.0186532528, 0.0107103038,
            0.0004257334, 6.17209e-17, 0.0008278439, 3.12513e-47,
            0.2461805610, 0.0004095694, 0.0000167770, 3.28408e-30]
        self.pvalues = np.reshape(pvalues, (6,-1))
        self.conf_int = [[[-0.0787282, 0.0556562], [0.1142092, 0.4812195],
            [-0.0377335, -0.0121565], [-0.0617356, 0.2267185], [-0.0293649,
            0.0397580], [-1.6078610, 0.8610574]], [[-0.1655059, -0.0119954],
            [0.1795247,	0.6038126], [-0.0384099, -0.0073858], [0.0138787,
            0.3482068], [0.0042042,	0.0915438], [-3.7467380, -0.7550884]],
            [[-0.2177596, 0.0058262], [0.2627019,	0.8841991], [-0.0370602,
            0.0073578], [-0.2546789, 0.2403740], [-0.0083075, 0.1234578],
            [-5.9323630,-1.3988040]],[[-0.1773841, -0.0057293], [1.0261390,
            1.5314040], [-0.0251818, 0.0078191], [0.0153462,	0.3843097],
            [0.0331544,	0.1358423], [-9.4906670, -5.7370190]], [[-0.1704124,
            -0.0161568], [1.1172810,	1.5766420], [-0.0328214, -0.0029868],
            [0.0503282,	0.3835495], [0.0359261,	0.1259907], [-8.7154010,
            -5.4055560]], [[-0.2234697, -0.0582916], [1.7890040, 2.3511560],
            [-0.0253747, 0.0065094], [0.1433769, 0.5004745], [0.0593053,
            0.1584829], [-14.1832200, -10.0282800]]]

class Spector():
    """
    Results are from Stata 11
    """
    def __init__(self):
        self.nobs = 32

    def logit(self):
        self.params = [2.82611297201, .0951576702557, 2.37868772835,
                -13.0213483201]
        self.cov_params = [[1.59502033639, -.036920566629, .427615725153,
                -4.57347950298], [-.036920566629, .0200375937069,
                .0149126464275, -.346255757562], [.427615725153 ,
                .0149126464275, 1.13329715236, -2.35916128427],
                [-4.57347950298, -.346255757562, -2.35916128427,
                24.3179625937]]
        self.bse = [1.26294114526, .141554207662, 1.06456430165, 4.93132462871]
        self.llf = -12.8896334653335
        self.llnull = -20.5917296966173
        self.df_model = 3
        self.df_resid = 32 - 4  #TODO: is this right? not reported in stata
        self.llr = 15.4041924625676
        self.prsquared = .374038332124624
        self.llr_pvalue = .00150187761112892
        self.aic = 33.779266930667
        self.bic = 39.642210541866
        self.z = [2.237723415, 0.6722348408, 2.234423721, -2.640537645]
        self.conf_int = [[.3507938,5.301432],[-.1822835,.3725988],[.29218,
                4.465195],[-22.68657,-3.35613]]
        self.pvalues = [.0252390974, .5014342039, .0254552063, .0082774596]
        self.margeff_nodummy_dydx = [.36258084688424,.01220841099085,
                .30517768382304]
        self.margeff_nodummy_dydxmean = [.53385885781692,.01797548988961,
                .44933926079386]
        self.margeff_nodummy_dydxmedian = [.25009492465091,.00842091261329,
                .2105003352955]

        self.margeff_nodummy_dydxzero = [6.252993785e-06,2.105437138e-07,
                5.263030788e-06]
        self.margeff_nodummy_dyex = [1.1774000792198,.27896245178384,
                .16960002159996]
        self.margeff_nodummy_dyexmean = [1.6641381583512,.39433730945339,
                .19658592659731]
        self.margeff_nodummy_dyexmedian = [.76654095836557,.18947053379898,0]
        self.margeff_nodummy_dyexzero = [0,0,0]
        self.margeff_nodummy_eydx = [1.8546366266779,.06244722072812,
                1.5610138123033]
        self.margeff_nodummy_eydxmean = [2.1116143062702,.0710998816585,
                1.7773072368626]
        self.margeff_nodummy_eydxmedian = [2.5488082240624,.0858205793373,
                2.1452853812126]
        self.margeff_nodummy_eydxzero = [2.8261067189993,.0951574597115,
                2.3786824653103]
        self.margeff_nodummy_eyex = [5.4747106798973,1.3173389907576,
                .44600395466634]
        self.margeff_nodummy_eyexmean = [6.5822977203268,1.5597536538833,
                .77757191612739]
        self.margeff_nodummy_eyexmedian = [7.8120973525952,1.9309630350892,0]
        self.margeff_nodummy_eyexzero = [0,0,0]
        # for below GPA = 2.0, psi = 1
        self.margeff_nodummy_atexog1 = [.1456333017086,.00490359933927,
                .12257689308426]
        # for below GPA at mean, tuce = 21, psi = 0
        self.margeff_nodummy_atexog2 = [.25105129214546,.00845311433473,
                .2113052923675]
        self.margeff_dummy_dydx = [.36258084688424,.01220841099085,
                .35751515254729]
        self.margeff_dummy_dydxmean = [.53385885781692,.01797548988961,
                .4564984096959]
#        self.margeff_dummy_dydxmedian
#        self.margeff_dummy_dydxzero
        self.margeff_dummy_eydx = [1.8546366266779,.06244722072812,
                1.5549034398832]
        self.margeff_dummy_eydxmean = [2.1116143062702,.0710998816585,
                1.6631775707188]
#        self.margeff_dummy_eydxmedian
#        self.margeff_dummy_eydxzero
# Factor variables not allowed in below
#        self.margeff_dummy_dyex
#        self.margeff_dummy_dyexmean
#        self.margeff_dummy_dyexmedian
#        self.margeff_dummy_dyexzero
#        self.margeff_dummy_eyex
#        self.margeff_dummy_eyex
#        self.margeff_dummy_eyex
#        self.margeff_dummy_eyex
        # for below GPA = 2.0, psi = 1
        self.margeff_dummy_atexog1 = [.1456333017086,.00490359933927,
                .0494715429937]
        # for below GPA at mean, tuce = 21, psi = 0
        self.margeff_dummy_atexog2 = [.25105129214546,.00845311433473,
                .44265645632553]

    def probit(self):
        self.params = [1.62581025407, .051728948442, 1.42633236818,
                -7.45232041607]
        self.cov_params =    [[.481472955383, -.01891350017, .105439226234,
            -1.1696681354], [-.01891350017, .00703757594, .002471864882,
            -.101172838897], [.105439226234, .002471864882, .354070126802,
            -.594791776765], [-1.1696681354, -.101172838897, -.594791776765,
            6.46416639958]]
        self.bse = [.693882522754, .083890261293, .595037920474, 2.54247249731]
        self.llf = -12.8188033249334
        self.llnull = -20.5917296966173
        self.df_model = 3
        self.df_resid = 32 - 4
        self.llr = 15.5458527433678
        self.prsquared = .377478069409622
        self.llr_pvalue = .00140489496775855
        self.aic = 33.637606649867
        self.bic = 39.500550261066
        self.z = [ 2.343062695, .6166263836, 2.397044489, -2.931131182]
        self.conf_int = [[.2658255,2.985795],[-.1126929,.2161508],[.2600795,
            2.592585],[-12.43547,-2.469166]]
        self.pvalues = [.0191261688, .537481188, .0165279168, .0033773013]

class RandHIE():
    """
    Results obtained from Stata 11
    """
    def __init__(self):
        self.nobs = 20190

    def poisson(self):
        self.params =   [-.052535114675, -.247086797633, .035290201794,
                -.03457750643, .271713973711, .033941474461, -.012635035534,
                .054056326828, .206115121809, .700352877227]
        self.cov_params = None
        self.bse = [.00288398915279, .01061725196728, .00182833684966,
                .00161284852954, .01223913844387, .00056476496963,
                .00925061122826, .01530987068312, .02627928267502,
                .01116266712362]
        self.llf = -62419.588535018
        self.llnull = -66647.181687959
        self.df_model = 9
        self.df_resid = self.nobs - self.df_model - 1
        self.llr = 8455.186305881856
        self.prsquared = .0634324369893758
        self.llr_pvalue = 0
        self.aic = 124859.17707
        self.bic = 124938.306497
        self.z = [-18.21612769, -23.27219872, 19.30180524, -21.43878101,
                22.20041672, 60.09840604, -1.36585953, 3.53081538, 7.84325525,
                62.74063980]
        self.conf_int = [[ -.0581876, -.0468826],[-0.2678962, -0.2262774],
                [0.0317067, 0.0388737],[-0.0377386, -0.0314164],
                [0.2477257, 0.2957022], [0.0328346, 0.0350484],[-0.0307659,
                    0.0054958], [0.0240495, 0.0840631],[0.1546087, 0.2576216],
                [0.6784745, 0.7222313]]
        self.pvalues = [3.84415e-74, 8.4800e-120, 5.18652e-83, 5.8116e-102,
                3.4028e-109, 0, .1719830562, .0004142808, 4.39014e-15, 0]