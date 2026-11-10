# Student Club Checker
from pyscript import display, document

def student_club(e):
    document.getElementById('result').innerHTML = ' '
    student_firstname  = document.getElementById('student_first').value
    student_lastname  = document.getElementById('student_last').value
    cocc_members_first = ['zoe', 'zarina', 'maryam', 'nathan', 'hans']
    cocc_members_last = ['reyes', 'perez', 'ledesma', 'bautista', 'baquiran']
    member_checker = student_firstname in cocc_members_first
    member_checker = student_lastname in cocc_members_last


    display_message = (f'Sorry you name is not on the list', f'Congratulations {student_firstname}  {student_lastname}! You are now part of COCC.')

    display(display_message[member_checker], target='result')

#Working with dictionary
from pyscript import display, document

def element_check(e):
    element = document.getElementById('elementname').value

    H = {
        'Symbol':'H',
        'Element Name':'Hydrogen',
        'Atomic Number':'1',
        'Atomic Mass':'1.0079'
    }
    C = {
        'Symbol':'C',
        'Element Name':'Carbon',
        'Atomic Number':'6',
        'Atomic Mass':'12.0107'
    }
    N = {
        'Symbol':'N',
        'Element Name':'Nitrogen',
        'Atomic Number':'7',
        'Atomic Mass':'14.0067'
    }
    O = {
        'Symbol':'O',
        'Element Name':'Oxygen',
        'Atomic Number':'8',
        'Atomic Mass':'	15.9994'
    }
    P = {
        'Symbol':'P',
        'Element Name':'Phosphorus',
        'Atomic Number':'15',
        'Atomic Mass':'30.9738'
    }
    S = {
        'Symbol':'S',
        'Element Name':'Sulfur',
        'Atomic Number':'16',
        'Atomic Mass':'	32.065'
    }
    Se = {
        'Symbol':'Se',
        'Element Name':'Selenium',
        'Atomic Number':'34',
        'Atomic Mass':'78.96'
    }
    F = {
        'Symbol':'F',
        'Element Name':'Fluorine',
        'Atomic Number':'9',
        'Atomic Mass':'18.9984'
    }
    Cl= {
        'Symbol':'Cl',
        'Element Name':'Chlorine',
        'Atomic Number':'17',
        'Atomic Mass':'35.453'
    }
    Br = {
        'Symbol':'Br',
        'Element Name':'Bromine',
        'Atomic Number':'35',
        'Atomic Mass':'	79.904'
    }
    I = {
        'Symbol':'I',
        'Element Name':'Iodine',
        'Atomic Number':'53',
        'Atomic Mass':'	126.9045'
    }
    At = {
        'Symbol':'At',
        'Element Name':'Astatine',
        'Atomic Number':'85',
        'Atomic Mass':'210'
    }
    Ts = {
        'Symbol':'Ts',
        'Element Name':'Tennessine',
        'Atomic Number':'117',
        'Atomic Mass':'294'
    }
    He = {
        'Symbol':'He',
        'Element Name':'Helium',
        'Atomic Number':'2',
        'Atomic Mass':'	4.0026'
    }
    Ne = {
        'Symbol':'Ne',
        'Element Name':'Neon',
        'Atomic Number':'10',
        'Atomic Mass':'	20.1797'
    }
    Ar = {
        'Symbol':'Ar',
        'Element Name':'Argon',
        'Atomic Number':'18',
        'Atomic Mass':'39.948'
    }
    Kr = {
        'Symbol':'Kr',
        'Element Name':'Krypton',
        'Atomic Number':'36',
        'Atomic Mass':'	83.798'
    }
    Xe = {
        'Symbol':'Xe',
        'Element Name':'Xenon',
        'Atomic Number':'54',
        'Atomic Mass':'	131.293'
    }
    Rn = {
        'Symbol':'Rn',
        'Element Name':'Radon',
        'Atomic Number':'86',
        'Atomic Mass':'222'
    }
    Og = {
        'Symbol':'Og',
        'Element Name':'Oganesson',
        'Atomic Number':'118',
        'Atomic Mass':'294'
    }  

    elements = {
        'H': H,
        'C': C,
        'N': N,
        'O': O,
        'P': P,
        'S': S,
        'Se': Se,
        'F': F,
        'Cl': Cl,
        'Br': Br,
        'I': I,
        'At': At,
        'Ts': Ts,
        'He': He,
        'Ne': Ne,
        'Ar': Ar,
        'Kr': Kr,
        'Xe': Xe,
        'Rn': Rn,
        'Og': Og
    }

    result = elements.get(element, 'That does not exist in the non-metals list.')
    display(result, target='output')

# Set operators
from pyscript import display, document

def student_name(e):
    first  = document.getElementById('firstname').value
    last  = document.getElementById('lastname').value

    grade7_members = {'Alex Santos', 'Gabriella Lopez'}
    grade8_members = {'Carlos Agap', 'Diana Cruz'} 
    grade9_members =     {'Oshri Gonzales', 'Rico Gozum', 'Jamielle Orduna'}
    grade10_members = {'Zoe Reyes', 'Zarina Perez', 'Maryam Ledesma', 'Hans Baquiran', 'Nathan Bautista'}

    display_new = {f'{first} {last}'} 

    all_members = grade7_members | grade8_members | grade9_members | grade10_members | display_new

    document.getElementById('result').innerHTML = (f"""
        <h3>All members:</h3>                                         
        {(', ').join(all_members)}
        <br>
        <h3>Total Number of Members:</h3>
        {len(all_members)}
    """) 
    # Debugged by AI instead of using (f'') used (f""") https://chatgpt.com/share/6af333c8-5b7c-83ec-98b0-15edd7f290b2 "can u debug"


       