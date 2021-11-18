# Run the script with...
# run rehman_becher_assignment2_task3_code.py
# color_h

from pymol import cmd
from PIL import ImageColor

def color(str):
    x = ImageColor.getcolor(str, "RGB")
    print(x)
    newList = []
    for i in range(0, len(x)):
        newList.append(x[i]/255)
    return newList

def color_h(selection='all'):
    s = str(selection)
    print(s)
    cmd.set_color('color_ile', color('#ff0000'))
    cmd.set_color('color_phe', color('#cb0034'))
    cmd.set_color('color_val', color('#f60009'))
    cmd.set_color('color_leu', color('#ea0015'))
    cmd.set_color('color_trp', color('#5b00a4'))
    cmd.set_color('color_met', color('#b0004f'))
    cmd.set_color('color_ala', color('#ad0052'))
    cmd.set_color('color_gly', color('#6a0095'))
    cmd.set_color('color_cys', color('#c2003d'))
    cmd.set_color('color_tyr', color('#4f00b0'))
    cmd.set_color('color_pro', color('#4600b9'))
    cmd.set_color('color_thr', color('#61009e'))
    cmd.set_color('color_ser', color('#5e00a1'))
    cmd.set_color('color_his', color('#1500ea'))
    cmd.set_color('color_glu', color('#0c00f3'))
    cmd.set_color('color_asn', color('#0c00f3'))
    cmd.set_color('color_gln', color('#0c00f3'))
    cmd.set_color('color_asp', color('#0c00f3'))
    cmd.set_color('color_lys', color('#0000ff'))
    cmd.set_color('color_arg', color('#0000ff'))
    cmd.color("color_ile", "(" + s + " and resn ile)")
    cmd.color("color_phe", "(" + s + " and resn phe)")
    cmd.color("color_val", "(" + s + " and resn val)")
    cmd.color("color_leu", "(" + s + " and resn leu)")
    cmd.color("color_trp", "(" + s + " and resn trp)")
    cmd.color("color_met", "(" + s + " and resn met)")
    cmd.color("color_ala", "(" + s + " and resn ala)")
    cmd.color("color_gly", "(" + s + " and resn gly)")
    cmd.color("color_cys", "(" + s + " and resn cys)")
    cmd.color("color_tyr", "(" + s + " and resn tyr)")
    cmd.color("color_pro", "(" + s + " and resn pro)")
    cmd.color("color_thr", "(" + s + " and resn thr)")
    cmd.color("color_ser", "(" + s + " and resn ser)")
    cmd.color("color_his", "(" + s + " and resn his)")
    cmd.color("color_glu", "(" + s + " and resn glu)")
    cmd.color("color_asn", "(" + s + " and resn asn)")
    cmd.color("color_gln", "(" + s + " and resn gln)")
    cmd.color("color_asp", "(" + s + " and resn asp)")
    cmd.color("color_lys", "(" + s + " and resn lys)")
    cmd.color("color_arg", "(" + s + " and resn arg)")
cmd.extend('color_h', color_h)
