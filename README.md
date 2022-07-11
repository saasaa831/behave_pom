# Design Pattern used is Python Behave Page Object model.
1. Test project based on this Test file Sample Test project.pdf (Pls see attached for ref)

Selenium webdriver , python , behave  
install latest Python or above 3.4.2 and all libraries installed with the pip

# Instructions below to run the code and attached sample results to check  [./reports]
1. git clone or download the zip.
3. Install Python 2.7 or higher.
4. Install behave and other libs from requirements.text
5. Complete installing Selenium webdriver components
6. Try change and use your github login credentials[username and password] under "features/Login.feature" file.
6. Open a shell/command prompt and from the root folder run "behave features --no-capture" ( delete reports folder before run)
7. To generate junit report run "behave --junit" [junit report regenerated on "./reports"]
   
# To generate Html report[go to reports folder]
1. Run junit2html TESTS-Login.xml testreport.html [junit xml must be ready to generate html]

# Alternatively, To render test summary of results in command line.[need junit xml report to proceed]
1. Run junit2html TESTS-Login.xml --summary-matrix
