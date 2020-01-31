# -#- coding: utf-8 -#-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

## @brief Module implementing a LED widget.
#
# It was inspired by KLed.
#


from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, Qt, QSize, QPoint
from PyQt5.QtGui import QColor, QRadialGradient, QPalette, QPainter, QBrush
from PyQt5.QtWidgets import QWidget

E5LedRectangular = 0
E5LedCircular = 1


## @brief     Class implementing a LED widget.
#

class E5Led(QWidget):
    ## \brief         Constructor
    #
    # @param parent reference to parent widget (QWidget)
    # @param color color of the LED (QColor)
    # @param shape shape of the LED (E5LedCircular, E5LedRectangular)
    # @param rectRatio ratio width to height, if shape is rectangular (float)
    #

    def __init__(self, parent=None, color=None, shape=E5LedCircular,
                 rectRatio=1):
        super(E5Led, self).__init__(parent)

        if color is None:
            color = QColor("green")
        ## @var __led_on
        # a member variable
        self.__led_on = True
        ## @var __dark_factor
        # a member variable
        self.__dark_factor = 300

    ## @brief         Protected slot handling the paint event.
    #
    # @param evt paint event object (QPaintEvent)
    # @exception TypeError The E5Led has an unsupported shape type.
    #

    def paintEvent(self, evt):
        if self.__shape == E5LedCircular:
            self.__paintRound()
        elif self.__shape == E5LedRectangular:
            self.__paintRectangular()
        else:
            raise TypeError("Unsupported shape type for E5Led.")

    # @private

    def __paintRectangular(self):
        # Initialize coordinates, width and height of the LED
        width = self.height()  # self.__rectRatio
        left = max(0, int((self.width() - width) / 2) - 1)
        right = min(int((self.width() + width) / 2), self.width())
        height = self.height()

        # now do the drawing
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        color = self.__led_on and self.__led_color or self.__offcolor

        painter.setPen(color.lighter(200))
        painter.drawLine(left, 0, left, height - 1)
        painter.drawLine(left + 1, 0, right - 1, 0)
        if self.__framedLed:
            painter.setPen(self.palette().color(QPalette.Dark))
        else:
            painter.setPen(color.darker())
        painter.drawLine(left + 1, height - 1, right - 1, height - 1)
        painter.drawLine(right - 1, 1, right - 1, height - 1)
        painter.fillRect(left + 1, 1, right - 2, height - 2, QBrush(color))
        painter.end()

    ## @brief         Public method to return the LED state.
    #
    # @return flag indicating the light state (boolean)
    #

    def setDarkFactor(self, darkfactor):
        if self.__dark_factor != darkfactor:
            self.__dark_factor = darkfactor
            self.__offcolor = self.__led_color.darker(darkfactor)
            self.update()

    ## @brief         Public method to return the dark factor.
    #
    # @return the current dark factor (integer)
    #

    def darkFactor(self):
        return self.__dark_factor

    """
    ############################################################## # ↓
    ## test group
    ############################################################## # ↑
    """

    ## \addtogroup mygrp YAHAHAH
    #  Additional documentation for group 'mygrp'
    #  @{
    #

    ##!
    #  A function
    #
    def func1(self):
        """"""

    ## Another function
    def func2(self):
        """"""

    ## @}

    """
    ############################################################## # ↓
    ## test Multiple lines.
    ############################################################## # ↑
    """
    #  must need '##'?
    #  so show.
    #
    def func31(self):
        """"""

    ##  line 1
    #  A function
    #  line 2
    def func32(self):
        """"""

    ##  line 1 \n
    #  A function \n
    #  line 2
    def func33(self):
        """"""

    ##  line 1 <br>
    #  A function <br>
    #  line 2
    def func34(self):
        """"""


## @brief     Class implementing a clickable LED widget.
#
#    @signal clicked(QPoint) emitted upon a click on the LED with the
#        left button
#    @signal middleClicked(QPoint) emitted upon a click on the LED with
#        the middle button or CTRL and left button
#

class E5ClickableLed(E5Led):
    clicked = pyqtSignal(QPoint)
    middleClicked = pyqtSignal(QPoint)

    ## @brief         Constructor
    #
    # @param parent reference to parent widget (QWidget)
    # @param color color of the LED (QColor)
    # @param shape shape of the LED (E5LedCircular, E5LedRectangular)
    # @param rectRatio ratio width to height, if shape is rectangular (float)
    #

    def __init__(self, parent=None, color=None, shape=E5LedCircular,
                 rectRatio=1):
        super(E5ClickableLed, self).__init__(parent, color, shape, rectRatio)

        self.setCursor(Qt.PointingHandCursor)
