from pymol import cmd

cmd.load("5TVN.pdb")

cmd.color('yellow', 'all')
cmd.remove('solvent')
cmd.color('gray70', 'organic')
cmd.select('ligands' , 'organic')

cmd.show_as(string representation, string selection)
