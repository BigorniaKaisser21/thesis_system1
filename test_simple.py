from simple_dart_fix import SimpleDartFix

# Your exact OCR output
ocr_output = """Void main ( ) {
for (int i > 0_i45;i# ){ Prin} Heration numbcr : si )"""

print("=" * 60)
print("INPUT:")
print("=" * 60)
print(ocr_output)

print("\n" + "=" * 60)
print("OUTPUT:")
print("=" * 60)
result = SimpleDartFix.fix(ocr_output)
print(result)

print("\n" + "=" * 60)
print("EXPECTED:")
print("=" * 60)
expected = """void main() {
    for (int i = 0; i < 5; i++) {
        print("Iteration number : $i");
    }
}"""
print(expected)

if result.strip() == expected.strip():
    print("\n✅ SUCCESS!")
else:
    print("\n❌ FAILED")