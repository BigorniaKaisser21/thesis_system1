from handwriting_fixes import HandwritingFixer
import sys

# Fix console encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

# Test Case 1: Dart void main for loop pattern
test1 = """Void main ( ) {
for (int i > 0_i45;i# ){ 
Prin} Heration numbcr : si )"""

# Test Case 2: Fruits pattern
test2 = """1) banana
frvits = ["apple' 5or frvit in frvits Print (frvit)
cherry"""

# Test Case 3: Number if-else pattern
test3 = """nimbtr int (inpul ( Enter 0 number :
2f humber %% 2 == 0_ (f"Lnvnber}" )1 Prut ic even clse print(f "Lwvmbt } it edd Il"""

# Test Case 4: Hello World pattern
test4 = """Pcil Hell: Wo(VA Jme = Io ( 16 L+ Rnlt"""

# Test Case 5: String concatenation pattern
test5 = """if number % 2 == 0:
    print("C f" "d number is even")
else:
    print("f " "d number is odd")"""

tests = [test1, test2, test3, test4, test5]
test_names = ["Dart Void Main", "Fruits List", "If-Else Number", "Hello World", "String Concatenation"]

for i, (name, test) in enumerate(zip(test_names, tests), 1):
    print(f"\n{'='*60}")
    print(f"TEST CASE {i}: {name}")
    print(f"{'='*60}")
    print("INPUT:")
    print("-" * 40)
    print(test)
    print("-" * 40)
    print("\nOUTPUT:")
    print("-" * 40)
    result = HandwritingFixer.fix_all(test)
    print(result)
    print("-" * 40)
    print(f"{'='*60}")