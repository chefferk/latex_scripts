
logic = ' |- p <-> (p & (q v ~q))'
# x = logic.replace('~', ' \\neg ')
# print(x)


def swap(convertions, logic):
    logic = logic.replace(' ', '')
    for i in range(len(convertions)):
        logic = logic.replace(convertions[i][2], convertions[i][1])
    return logic


def logic_print(logic):
    print('${}$\\\\' .format(logic))


convertions = [['or',        ' \\vee ',              'v'],
               ['not',       ' \\equiv ',            '-||-'],
               ['yields',    ' \\vdash ',            '|-'],
               ['not',       ' \\neg ',              '~'],
               ['and',       ' \\wedge ',            '&'],
               ['implies',   ' \\to ',               '->'],
               ['iff',       ' \\leftrightarrow ',   '<->'],
               ['all',       ' \\forall ',           '@'],
               ['some',      ' \\exists ',           '$']]

logic = swap(convertions, logic)
logic_print(logic)

rules = [
    ['RAA', '(Reductio ad Absurdum)', '(Reductio ad Absurdum)'],
    ['Neg<->', '(Negated<->)', 'Negated Biconditional'],
    ['<->I', '(Double-Arrow Intro)', 'Definition of Biconditional'],
    ['<->E', '(Double-Arrow Elim)', 'Definition of Biconditional'],
    ['A', '(Assumption)', 'Premise'],
    ['&I', '(Ampersand Intro)', 'Conjunction'],
    ['&E', '(Ampersand Elim)', 'Simplification'],
    ['vI', '(Wedge Intro)', 'Addition'],
    ['vE', '(Wedge Elim)', 'Disjunctive Syllogism'],
    ['->I', '(Arrow Intro)', '(Arrow Intro)'],
    ['->E', '(Arrow Elim)', 'Modus Pones'],
    ['@E', '(Universal Elim)', 'Universal Instantiation'],
    ['@I', '(Universal Intro)', 'Universal Generalization'],
    ['$I', '(Existential Intro)', 'Existential Generalization'],
    ['$E', '(Existential Elim)', 'Existential Instantiation'],
    ['=I', '(Identity Intro)', '(Identity Intro)'],
    ['=E', '(Identity Elim)', '(Identity Elim)'],
    ['DN', '(Double Negation)', 'Double Negation'],
    ['MTT', '(Modus Tollendo Tollens)', 'Modus Tollens'],
    ['HS', '(Hypothetical Syllogism)', 'Hypothetical Syllogism'],
    ['TC', '(True Consequent)', '(True Consequent)'],
    ['FA', '(False Antecedent)', '(False Antecedent)'],
    ['IA', '(Impossible Antecedent)', '(Impossible Antecedent)'],
    ['v->', '(Wedge Arrow)', 'Definition of Implication'],
    ['SimDil', '(Simple Dilemma)', '(Simple Dilemma)'],
    ['ComDil', '(Complex Dilemma)', '(Complex Dilemma)'],
    ['SpecDil', '(Special Dilemma)', '(Special Dilemma)'],
    ['DM', '(DeMorgan)', 'De Morgan'],
    ['Neg->', '(Negated Arrow)', 'Negated Implication'],
    ['&Comm', '(& Commutativity)', 'Commutativity'],
    ['vComm', '(v Commutativity)', 'Commutativity'],
    ['<->Comm', '(<->Commutativity)', 'Commutativity'],
    ['Trans', '(Transposition)', 'Contrapositive'],
    ['&Assoc', '(& Associativity)', 'Associativity'],
    ['vAssoc', '(v Associativity)', 'Associativity'],
    ['&/vDist', '(&/v Distribution)', 'Distribution'],
    ['v/&Dist', '(v/& Distribution)', 'Distribution'],
    ['Imp/Exp', '(Imp/Exportation)', '(Imp/Exportation)'],
    ['BP', '(Biconditional Ponens)', '(Biconditional Ponens)'],
    ['BT', '(Biconditional Tollens)', '(Biconditional Tollens)'],
    ['BiTrans', '(BiTransposition)', 'Contrapositive'],
    ['QE', '(Quantifier Exchange)', 'De Morgan']]
