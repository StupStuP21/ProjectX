
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt



class PlotCanvas(FigureCanvas):
    def __init__(self, parent, width=5, height=4, dpi=100, scores= [1,2,3,4,5], koeffs= [5,4,3,2,1]):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        #FigureCanvas.setSizePolicy(self,
         #                          QSizePolicy.Expanding,
          #                         QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(scores, koeffs)

    def plot(self,scores, koeffs):
        #ax.plot(koeffs, scores)
        """
        newObject = ForGraphics(testId=1)
        """
        ax = self.figure.add_subplot(111)
        ax.scatter(koeffs,scores)
        #ax.plot(koeffs,scores)
        ax.set_title('График зависимости успешности выполнения контрольных работ от предполагаемой нами успешной стратегии')
        self.draw()
