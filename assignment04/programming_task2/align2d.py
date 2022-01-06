from modeller import *

env = Environ()

# Read in HETATM records from template PDBs
env.io.hetatm = True

aln = Alignment(env)
mdl = Model(env, file='template', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='templateA', atom_files='template.pdb')
aln.append(file='mutated_target.ali', align_codes='mutated_target')
aln.align2d()
aln.write(file='mutated_target-template.ali', alignment_format='PIR')
aln.write(file='mutated_target-template.pap', alignment_format='PAP')
