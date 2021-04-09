# Imports venn diagrams and pyplot from the matplot library
from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt

# Creates the venn diagram figures using array global variable
figure, (figure1, figure2) = plt.subplots(1, 2, figsize=(10, 10))
class setTheory():  # Creates the set theory class.

    def xor():  # creates the xor function
        # Uses subsets to set the size of the circles
        vennDiagram1 = venn2(subsets=(2,2,1,), ax=figure1)
        venn2_circles(subsets=(2, 2, 1), ax=figure1)

        # Creates array for loop to fill in the colour on the venn diagram. != means not equal to
        for area in {'01', '10', '11'}:
            colour = '#ffca08' if area != '11' else 'white'

            vennDiagram1.get_patch_by_id(area).set_color(colour)    # Sets the colour
            vennDiagram1.get_patch_by_id(area).set_alpha(1)         # Sets the alpha, 0 would be transparent
            txt = vennDiagram1.get_label_by_id(area)    # Used to label the areas
            if txt: txt.set_text('')

        figure1.set_axis_on()
        figure1.set_facecolor('white')
        figure1.set_title('XOR', fontsize=15)
        # Changes the position on the Y axis. 0.1 stops the text from overlapping the square
        ymin, ymax = figure1.get_ylim()
        figure1.set_ylim(ymin - 0.1, ymax)
        return vennDiagram1

    def nand(): # Creates the nand function
        vennDiagram2 = venn2(subsets=(2, 2, 1), ax=figure2)
        venn2_circles(subsets=(2, 2, 1), ax=figure2)

        for area in ['01', '10', '11']:
            colour = '#ffca08' if area != '11' else 'white'
            vennDiagram2.get_patch_by_id(area).set_color(colour)
            vennDiagram2.get_patch_by_id(area).set_alpha(1)
            txt = vennDiagram2.get_label_by_id(area)
            if txt: txt.set_text('')

        figure2.set_axis_on()
        figure2.set_facecolor('#ffca08')
        figure2.set_title('NAND', fontsize=15)
        ymin, ymax = figure2.get_ylim()
        figure2.set_ylim(ymin - 0.1, ymax)

    xor()
    nand()
setTheory()
plt.show()
