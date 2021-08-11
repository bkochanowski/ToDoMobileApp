"ToDoMobileApp" 

# 1. Installation instructions for Windows 10 
(Caution: dependencies for Linux distributions are slightly different but it is possible to run the code from Linux - readme will be updated shortly):
    
    1) create local project repository 
    2) set virtual enviroment
    3) install dependencies from requirements.txt
    4)  install additional packages from kivy.garden with terminal commands below:
         garden install --app circularlayout 
         garden install --app circulardatetimepicker
         garden install --app navigationdrawer
         garden install --app iconfonts
         Please veryfy paths to packages above in project's main.py, view.py, main.kv, __init__.py, since 
         new updates to kivy.garden might change path to package directory. Defaults route should be: 
         libs/garden/<package name>
    5) install Material Design Iconic Font package into location app/assets
       Newest package to download available here: 
       https://zavoloklom.github.io/material-design-iconic-font/index.html
    6) Now it should be possible to run the aplication from local repository.
    7) It is possible to make an APK package for android, via Buildozer project. Step-by-step tutorial is 
       available here: 
       https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android
       Be advised that buildozer project works under Linux distributions only. It was tested on Windows10 
       WSL on Ubuntu 20.04 distribution

# 2. Basic description:
    Mobile application implemented in Python 3.8 using the KIVY framework dedicated to Android devices, 
    but after compilation it should also work on the desktop/iOS. App consists of a simple interface with 
    a toolbar at the top that allows navigation between the two available screens:
        1) list of tasks
        2) list of products to buy.

    Each item of the task consists of a title, task details of the task and a deadline which consists of 
    date and time. The task widgets are meant to be displayed i 3 different colors depending on the date 
    of the assumed completion. Any missed tasks with an expired deadline are shown in red color, while 
    tasks for the current day are highlighted in yellow.

    In order to add a new task just select "dodaj zadanie" in the context menu. In this case, a new popup 
    window is displayed with a text field to fill and two interactive buttons for selecting the date and 
    time. If necessary, there is a feature that makes possible to update each of the above-mentioned data 
    in an already created task. There is a specific button for this. The application has the ability to 
    deselect already purchased products from the list - they are then graphically marked and separated from 
    other products still on the list.
    
# 3. Packages/projects used for this app

    -> KivyCalendar - slightly modded Datepicker module based on KivyCalendar meant for python 2.7 This 
    Widget is based on Oleg Kozlov (xxblx) work. Link:  https://bitbucket.org/xxblx/kivycalendar.
    
    -> NavigationDrawer - kivy.garden package which provides a hidden panel view designed to duplicate 
    popular Android layout. Link: https://github.com/kivy-garden/garden.navigationdrawer
    
    -> Circular Date & Time Picker for Kivy - kivy.garden widget which aim is to provide a date and time 
    selector similar to the one found in Android KitKat+. 
    Link: https://github.com/kivy-garden/garden.circulardatetimepicker
    
    -> Kivy-iconfonts - Simple helper functions to make easier to use icon fonts in Labels and derived 
    widgets. Link: https://github.com/kivy-garden/garden.iconfonts
    
