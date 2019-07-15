# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Forms\Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/rammc/.designer/backup/title.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mp = QtWidgets.QWidget()
        self.tab_mp.setObjectName("tab_mp")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_mp)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.tab_mp)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.txt_Cost_BlackStone_Weapon = QtWidgets.QLineEdit(self.widget_4)
        self.txt_Cost_BlackStone_Weapon.setObjectName("txt_Cost_BlackStone_Weapon")
        self.gridLayout.addWidget(self.txt_Cost_BlackStone_Weapon, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.txt_Cost_BlackStone_Armor = QtWidgets.QLineEdit(self.widget_4)
        self.txt_Cost_BlackStone_Armor.setObjectName("txt_Cost_BlackStone_Armor")
        self.gridLayout.addWidget(self.txt_Cost_BlackStone_Armor, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.txt_Cost_Conc_Weapon = QtWidgets.QLineEdit(self.widget_4)
        self.txt_Cost_Conc_Weapon.setObjectName("txt_Cost_Conc_Weapon")
        self.gridLayout.addWidget(self.txt_Cost_Conc_Weapon, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.txt_Cost_ConcArmor = QtWidgets.QLineEdit(self.widget_4)
        self.txt_Cost_ConcArmor.setObjectName("txt_Cost_ConcArmor")
        self.gridLayout.addWidget(self.txt_Cost_ConcArmor, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)
        self.txt_Cost_MemFrag = QtWidgets.QLineEdit(self.widget_4)
        self.txt_Cost_MemFrag.setObjectName("txt_Cost_MemFrag")
        self.gridLayout.addWidget(self.txt_Cost_MemFrag, 4, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 1, 1, 1)
        self.txt_Cost_Cron = QtWidgets.QLineEdit(self.widget_4)
        self.txt_Cost_Cron.setObjectName("txt_Cost_Cron")
        self.gridLayout.addWidget(self.txt_Cost_Cron, 5, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 1, 1, 1)
        self.txt_Cost_Cleanse = QtWidgets.QLineEdit(self.widget_4)
        self.txt_Cost_Cleanse.setObjectName("txt_Cost_Cleanse")
        self.gridLayout.addWidget(self.txt_Cost_Cleanse, 6, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 205, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.tab_mp)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmdMonniesMP = QtWidgets.QPushButton(self.widget_5)
        self.cmdMonniesMP.setEnabled(False)
        self.cmdMonniesMP.setObjectName("cmdMonniesMP")
        self.horizontalLayout_4.addWidget(self.cmdMonniesMP)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.tabWidget.addTab(self.tab_mp, "")
        self.tab_fs_equip = QtWidgets.QWidget()
        self.tab_fs_equip.setObjectName("tab_fs_equip")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_fs_equip)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_FS = QtWidgets.QTableWidget(self.tab_fs_equip)
        self.table_FS.setAlternatingRowColors(True)
        self.table_FS.setObjectName("table_FS")
        self.table_FS.setColumnCount(6)
        self.table_FS.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS.setHorizontalHeaderItem(5, item)
        self.table_FS.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.table_FS)
        self.widget = QtWidgets.QWidget(self.tab_fs_equip)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmdFSAutoPrice = QtWidgets.QPushButton(self.widget)
        self.cmdFSAutoPrice.setEnabled(False)
        self.cmdFSAutoPrice.setCheckable(True)
        self.cmdFSAutoPrice.setObjectName("cmdFSAutoPrice")
        self.horizontalLayout.addWidget(self.cmdFSAutoPrice)
        self.cmdFSPrice = QtWidgets.QPushButton(self.widget)
        self.cmdFSPrice.setEnabled(False)
        self.cmdFSPrice.setObjectName("cmdFSPrice")
        self.horizontalLayout.addWidget(self.cmdFSPrice)
        self.cmdFSRemove = QtWidgets.QPushButton(self.widget)
        self.cmdFSRemove.setObjectName("cmdFSRemove")
        self.horizontalLayout.addWidget(self.cmdFSRemove)
        self.cmdFSAdd = QtWidgets.QPushButton(self.widget)
        self.cmdFSAdd.setObjectName("cmdFSAdd")
        self.horizontalLayout.addWidget(self.cmdFSAdd)
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.tab_fs_equip, "")
        self.tab_FS = QtWidgets.QWidget()
        self.tab_FS.setObjectName("tab_FS")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_FS)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.table_FS_Cost = QtWidgets.QTableWidget(self.tab_FS)
        self.table_FS_Cost.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_FS_Cost.setAlternatingRowColors(True)
        self.table_FS_Cost.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_FS_Cost.setObjectName("table_FS_Cost")
        self.table_FS_Cost.setColumnCount(6)
        self.table_FS_Cost.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS_Cost.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS_Cost.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS_Cost.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS_Cost.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS_Cost.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_FS_Cost.setHorizontalHeaderItem(5, item)
        self.table_FS_Cost.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.table_FS_Cost)
        self.widget_3 = QtWidgets.QWidget(self.tab_FS)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmdFSRefresh = QtWidgets.QPushButton(self.widget_3)
        self.cmdFSRefresh.setObjectName("cmdFSRefresh")
        self.horizontalLayout_3.addWidget(self.cmdFSRefresh)
        self.cmdFS_Cost_Clear = QtWidgets.QPushButton(self.widget_3)
        self.cmdFS_Cost_Clear.setObjectName("cmdFS_Cost_Clear")
        self.horizontalLayout_3.addWidget(self.cmdFS_Cost_Clear)
        self.cmdFSEdit = QtWidgets.QPushButton(self.widget_3)
        self.cmdFSEdit.setObjectName("cmdFSEdit")
        self.horizontalLayout_3.addWidget(self.cmdFSEdit)
        self.cmdFSGraph = QtWidgets.QPushButton(self.widget_3)
        self.cmdFSGraph.setEnabled(False)
        self.cmdFSGraph.setObjectName("cmdFSGraph")
        self.horizontalLayout_3.addWidget(self.cmdFSGraph)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.tabWidget.addTab(self.tab_FS, "")
        self.tab_equip = QtWidgets.QWidget()
        self.tab_equip.setObjectName("tab_equip")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_equip)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table_Equip = QtWidgets.QTableWidget(self.tab_equip)
        self.table_Equip.setAlternatingRowColors(True)
        self.table_Equip.setObjectName("table_Equip")
        self.table_Equip.setColumnCount(8)
        self.table_Equip.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Equip.setHorizontalHeaderItem(7, item)
        self.table_Equip.horizontalHeader().setCascadingSectionResizes(False)
        self.table_Equip.horizontalHeader().setSortIndicatorShown(True)
        self.table_Equip.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.table_Equip)
        self.widget_2 = QtWidgets.QWidget(self.tab_equip)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmdEquipAutoPrice = QtWidgets.QPushButton(self.widget_2)
        self.cmdEquipAutoPrice.setEnabled(False)
        self.cmdEquipAutoPrice.setObjectName("cmdEquipAutoPrice")
        self.horizontalLayout_2.addWidget(self.cmdEquipAutoPrice)
        self.cmdEquipPrice = QtWidgets.QPushButton(self.widget_2)
        self.cmdEquipPrice.setEnabled(False)
        self.cmdEquipPrice.setObjectName("cmdEquipPrice")
        self.horizontalLayout_2.addWidget(self.cmdEquipPrice)
        self.cmdEquipCost = QtWidgets.QPushButton(self.widget_2)
        self.cmdEquipCost.setEnabled(False)
        self.cmdEquipCost.setObjectName("cmdEquipCost")
        self.horizontalLayout_2.addWidget(self.cmdEquipCost)
        self.cmdEquipRemove = QtWidgets.QPushButton(self.widget_2)
        self.cmdEquipRemove.setObjectName("cmdEquipRemove")
        self.horizontalLayout_2.addWidget(self.cmdEquipRemove)
        self.cmdEquipAdd = QtWidgets.QPushButton(self.widget_2)
        self.cmdEquipAdd.setObjectName("cmdEquipAdd")
        self.horizontalLayout_2.addWidget(self.cmdEquipAdd)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tab_equip, "")
        self.tab_strat = QtWidgets.QWidget()
        self.tab_strat.setObjectName("tab_strat")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_strat)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.tab_strat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.table_Strat = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Strat.sizePolicy().hasHeightForWidth())
        self.table_Strat.setSizePolicy(sizePolicy)
        self.table_Strat.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.table_Strat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_Strat.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_Strat.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_Strat.setObjectName("table_Strat")
        self.table_Strat.setColumnCount(3)
        self.table_Strat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat.setHorizontalHeaderItem(2, item)
        self.table_Strat.verticalHeader().setVisible(False)
        self.widget_6 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.table_Strat_FS = QtWidgets.QTableWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Strat_FS.sizePolicy().hasHeightForWidth())
        self.table_Strat_FS.setSizePolicy(sizePolicy)
        self.table_Strat_FS.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_Strat_FS.setAlternatingRowColors(True)
        self.table_Strat_FS.setObjectName("table_Strat_FS")
        self.table_Strat_FS.setColumnCount(3)
        self.table_Strat_FS.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_FS.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_FS.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_FS.setHorizontalHeaderItem(2, item)
        self.table_Strat_Equip = QtWidgets.QTableWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Strat_Equip.sizePolicy().hasHeightForWidth())
        self.table_Strat_Equip.setSizePolicy(sizePolicy)
        self.table_Strat_Equip.setAlternatingRowColors(True)
        self.table_Strat_Equip.setObjectName("table_Strat_Equip")
        self.table_Strat_Equip.setColumnCount(5)
        self.table_Strat_Equip.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_Equip.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_Equip.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_Equip.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_Equip.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Strat_Equip.setHorizontalHeaderItem(4, item)
        self.verticalLayout_7.addWidget(self.splitter_2)
        self.verticalLayout_6.addWidget(self.splitter)
        self.widget_7 = QtWidgets.QWidget(self.tab_strat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cmd_Strat_Graph = QtWidgets.QPushButton(self.widget_7)
        self.cmd_Strat_Graph.setObjectName("cmd_Strat_Graph")
        self.horizontalLayout_5.addWidget(self.cmd_Strat_Graph)
        self.cmdStrat_go = QtWidgets.QPushButton(self.widget_7)
        self.cmdStrat_go.setObjectName("cmdStrat_go")
        self.horizontalLayout_5.addWidget(self.cmdStrat_go)
        self.verticalLayout_6.addWidget(self.widget_7)
        self.tabWidget.addTab(self.tab_strat, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_XLSX = QtWidgets.QAction(MainWindow)
        self.actionExport_XLSX.setEnabled(False)
        self.actionExport_XLSX.setObjectName("actionExport_XLSX")
        self.actionSave_Info = QtWidgets.QAction(MainWindow)
        self.actionSave_Info.setObjectName("actionSave_Info")
        self.actionLoad_Info = QtWidgets.QAction(MainWindow)
        self.actionLoad_Info.setObjectName("actionLoad_Info")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFail_Stack_Graph = QtWidgets.QAction(MainWindow)
        self.actionFail_Stack_Graph.setEnabled(False)
        self.actionFail_Stack_Graph.setObjectName("actionFail_Stack_Graph")
        self.actionCost_Graph = QtWidgets.QAction(MainWindow)
        self.actionCost_Graph.setEnabled(False)
        self.actionCost_Graph.setObjectName("actionCost_Graph")
        self.actionEfficiency_Graph = QtWidgets.QAction(MainWindow)
        self.actionEfficiency_Graph.setEnabled(False)
        self.actionEfficiency_Graph.setObjectName("actionEfficiency_Graph")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGitHub_README = QtWidgets.QAction(MainWindow)
        self.actionGitHub_README.setObjectName("actionGitHub_README")
        self.actionWindow_Always_on_Top = QtWidgets.QAction(MainWindow)
        self.actionWindow_Always_on_Top.setCheckable(True)
        self.actionWindow_Always_on_Top.setObjectName("actionWindow_Always_on_Top")
        self.actionExport_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_CSV.setObjectName("actionExport_CSV")
        self.actionExport_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_Excel.setObjectName("actionExport_Excel")
        self.menuFile.addAction(self.actionSave_Info)
        self.menuFile.addAction(self.actionLoad_Info)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_CSV)
        self.menuFile.addAction(self.actionExport_Excel)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionFail_Stack_Graph)
        self.menuView.addAction(self.actionCost_Graph)
        self.menuView.addAction(self.actionEfficiency_Graph)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionWindow_Always_on_Top)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionGitHub_README)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enhancement Optimizer"))
        self.label_2.setText(_translate("MainWindow", "Black Stone (Weapon)"))
        self.label_5.setText(_translate("MainWindow", "Black Stone (Armor)"))
        self.label_7.setText(_translate("MainWindow", "Concentrated Magical Blackstone (Weapon)"))
        self.label_9.setText(_translate("MainWindow", "Concentrated Magical Blackstone (Armor)"))
        self.label_11.setText(_translate("MainWindow", "Memory Fragment"))
        self.label_12.setText(_translate("MainWindow", "Cron Stone"))
        self.label_14.setText(_translate("MainWindow", "Gear Cleanse Cost"))
        self.cmdMonniesMP.setText(_translate("MainWindow", "Refresh Prices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mp), _translate("MainWindow", "Monnies / MP"))
        item = self.table_FS.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_FS.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Gear Type"))
        item = self.table_FS.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.table_FS.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Level"))
        item = self.table_FS.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Max #"))
        item = self.table_FS.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sale Balance"))
        self.cmdFSAutoPrice.setText(_translate("MainWindow", "Auto Check Price"))
        self.cmdFSPrice.setText(_translate("MainWindow", "Check Price"))
        self.cmdFSRemove.setText(_translate("MainWindow", "Remove Item"))
        self.cmdFSAdd.setText(_translate("MainWindow", "Add Item"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fs_equip), _translate("MainWindow", "FS Gear"))
        item = self.table_FS_Cost.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FS"))
        item = self.table_FS_Cost.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Gear"))
        item = self.table_FS_Cost.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cost"))
        item = self.table_FS_Cost.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cumulitive Cost"))
        item = self.table_FS_Cost.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Probability"))
        item = self.table_FS_Cost.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cumulitive Probability"))
        self.cmdFSRefresh.setText(_translate("MainWindow", "Refresh"))
        self.cmdFS_Cost_Clear.setText(_translate("MainWindow", "Clear Selected Edits"))
        self.cmdFSEdit.setText(_translate("MainWindow", "Change Item"))
        self.cmdFSGraph.setText(_translate("MainWindow", "View Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_FS), _translate("MainWindow", "FS Cost"))
        item = self.table_Equip.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_Equip.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Gear Type"))
        item = self.table_Equip.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cost"))
        item = self.table_Equip.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Level"))
        item = self.table_Equip.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "FS"))
        item = self.table_Equip.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Enhance Cost"))
        item = self.table_Equip.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Num Fails"))
        item = self.table_Equip.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Uses Memfrags"))
        self.cmdEquipAutoPrice.setText(_translate("MainWindow", "Auto Check Price"))
        self.cmdEquipPrice.setText(_translate("MainWindow", "Check Price"))
        self.cmdEquipCost.setText(_translate("MainWindow", "Calculate Costs"))
        self.cmdEquipRemove.setText(_translate("MainWindow", "Remove"))
        self.cmdEquipAdd.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_equip), _translate("MainWindow", "Equiptment"))
        item = self.table_Strat.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FS"))
        item = self.table_Strat.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item"))
        item = self.table_Strat.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Attempt?"))
        item = self.table_Strat_FS.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.table_Strat_FS.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cost"))
        item = self.table_Strat_FS.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Effectiveness"))
        item = self.table_Strat_Equip.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.table_Strat_Equip.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cost"))
        item = self.table_Strat_Equip.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loss Prevention"))
        item = self.table_Strat_Equip.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Avg Num Fails"))
        item = self.table_Strat_Equip.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Success Confidence"))
        self.cmd_Strat_Graph.setText(_translate("MainWindow", "Graphs"))
        self.cmdStrat_go.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_strat), _translate("MainWindow", "Strategy"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport_XLSX.setText(_translate("MainWindow", "Export XLSX"))
        self.actionSave_Info.setText(_translate("MainWindow", "Save Info"))
        self.actionLoad_Info.setText(_translate("MainWindow", "Load Info"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFail_Stack_Graph.setText(_translate("MainWindow", "Fail Stack Graph"))
        self.actionCost_Graph.setText(_translate("MainWindow", "Cost Graph"))
        self.actionEfficiency_Graph.setText(_translate("MainWindow", "Efficiency Graph"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionGitHub_README.setText(_translate("MainWindow", "GitHub - README"))
        self.actionWindow_Always_on_Top.setText(_translate("MainWindow", "Window Always on Top"))
        self.actionExport_CSV.setText(_translate("MainWindow", "Export CSV"))
        self.actionExport_Excel.setText(_translate("MainWindow", "Export Excel"))

