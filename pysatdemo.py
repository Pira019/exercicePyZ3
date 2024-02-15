from pysat.solvers import Glucose3, Solver
#creation d'un objet solveur 
s = Solver(name='g3')
#ajout de 2 clauses dans le solveur
# (non(x1) or x2) et (non(x1) or non(x2))
s.add_clause([1])
s.add_clause([-1])
#verification de la satisfiabilité
sat = s.solve()
if sat==True:
    print("satisfiable lors du cours")
    #affichage de l'évaluation qui prouve 
    #la satisfiabilité
    print(s.get_model())
else :
    print("non satisfiable")

