h5(strong("Income Type")),

p(strong("Household equivalised disposable income: "), "is calculated by dividing the total household disposable income by an equivalisation factor. TAWA uses the 'modified OECD' equivalence scale to estimate the equivalisation factor and applies a weight of 1.0 to the first adult in the household, 0.5 to other household members aged 14 and over, and 0.3 to those aged less than 14. A 'family' equivalised disposable income is also provided but results should be treated with caution as this calculation is not used in regular TAWA analysis/advice."), 

p(strong("Taxable income: "),"the sum of all core benefits (JSS, SLP, SPS), superannuation, student allowance, other taxable benefits, wage and salary income, redundancy income, self-employment income and other taxable income",strong("before"),"tax and any other deductions are removed. Note that negative income amounts are included when calculating taxable income though total taxable income is defined as greater than or equal to zero."),
  
p(strong("Total income: "),"is the sum of taxable income (see above), abated accommodation supplement, winter energy payment, other non-taxable benefits, non-taxable income, and working for family tax credits. Note working for family tax credits include FTC, IWTC, MFTC, PTC, Best Start and IETC."),

p(strong("Disposable income: "), "total income less tax and other deductions such as the ACC levy. Note negative incomes are included."),

br(),
                 
h5(strong("Population subgroups")),

p("In the population subgroups below, a child is defined using the Working for Family definition of a ‘dependent child’."),
p(" "),
p("For a selected population unit, i.e. household or family,"),

tags$ul(
tags$li(strong("Aged 0-15"),"indicates there is a least one individual aged 0-15 in the ‘population unit’"),
tags$li(strong("Aged 16-64"),"indicates there is a least one individual aged 16-64 in the ‘population unit’"),
tags$li(strong("Aged 65+"),"indicates there is a least one individual aged 16-64 in the ‘population unit’")),

tags$ul(
  tags$li(strong("Single with children"),"indicates that there is a single adult with children in the ‘population unit’"),
  tags$li(strong("Single without children"),"indicates that there is a single adult without children in the ‘population unit’"),
  tags$li(strong("Couple with children"),"indicates that there is a couple with children in the ‘population unit’"),
  tags$li(strong("Couple without children"),"indicates that there is a couple without with children in the ‘population unit’"),
  tags$li(strong("Multiple families with children"),"indicates that there are multiple families in the household with at least one family having at least one child."),
  tags$li(strong("Multiple families without children"),"indicates that there are multiple families in the household with no children.")),

tags$ul(
  tags$li(strong("With children"),"indicates that there are children in the ‘population unit’"),
  tags$li(strong("Without children"),"indicates that there are no children in the ‘population unit’")),

tags$ul(
  tags$li(strong("Accommodation supplement"),"indicates there is at least one individual receiving an Accommodation Supplement payment in the ‘population unit’"),
  tags$li(strong("Core benefits"),"indicates there is at least one individual receiving a core benefit (JSS, SLP, or SPS) in the ‘population unit’"),
  tags$li(strong("FTC"),"indicates there is at least one individual receiving a Family Tax Credit in the ‘population unit’"),
  tags$li(strong("IWTC"),"indicates there is at least one individual receiving a In Work Tax Credit in the ‘population unit’"),
tags$li(strong("MFTC"),"indicates there is at least one individual receiving a Minimum Family Tax Credit in the ‘population unit’"),
tags$li(strong("NZ Super"),"indicates there is at least one individual receiving NZ Superannuation in the ‘population unit’"),
tags$li(strong("WEP"),"indicates there is at least one individual receiving a Winter Energy Payment in the ‘population unit’"),
tags$li(strong("WFF"),"indicates there is at least one individual receiving Working for Families in the ‘population unit’")),

br(),
                 
h5(strong("Other")),
p(strong("Fixed income bands: "), "household / families are assigned an income band based on the income selected, e.g. disposable income. Each income band is of equal width (except for the  first and last income band) and has a different population size."),
p(strong("Ventiles: "), "the overall household (or family) population is separated into 20 equal groups based on the income selected, e.g. disposable income. The corresponding income bands (not currently provided) will be of different sizes with thinner income bands where the population is larger and wider income bands where the population is not as smaller.")
