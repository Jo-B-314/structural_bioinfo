fetch 1HDA

select chA, visible

# remove water
remove solvent

# color ligands gray
color gray40, organic

# select all ligands
select ligands, organic

# active site residues
show sticks, byres all within 5 of ligands

color white, all within 5 of ligands

color gray40, organic

hide cartoon, chA