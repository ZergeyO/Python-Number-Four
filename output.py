import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

class Output:
    def __init__(self, axis_x, axis_y):
        self.x=axis_x
        self.y=axis_y

    def makeplot(self):
        plt.plot(self.x, self.y)
        plt.xlabel('Frequency')
        plt.ylabel('RCS')
        plt.title('RCS from frequency')
        plt.grid()
        plt.show()

    def xml_saving(self):
        self.lamda=3e8/self.x
        import xml.etree.ElementTree as ET
        root = ET.Element("data")

        for i in range(len(self.x)):
            row = ET.SubElement(root, "row")
    
            freq_elem = ET.SubElement(row, "freq")
            freq_elem.text = str(self.x[i])
    
            lambda_elem = ET.SubElement(row, "lambda")
            lambda_elem.text = str(3e8/self.x[i])
    
            rcs_elem = ET.SubElement(row, "rcs")
            rcs_elem.text = str(self.y[i])
        tree = ET.ElementTree(root)
        tree.write("data.xml", encoding="utf-8", xml_declaration=True)  
