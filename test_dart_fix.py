from dart_fixes import DartFixer

# Your exact OCR output
ocr_output = """Void main ( ) {
for (int i > 0_i45;i# ){ Prin} Heration numbcr : si )"""

print("=" * 60)
print("ORIGINAL OCR OUTPUT:")
print("=" * 60)
print(ocr_output)

print("\n" + "=" * 60)
print("FIXED DART CODE:")
print("=" * 60)
result = DartFixer.fix_dart_code(ocr_output)
print(result)

print("\n" + "=" * 60)
print("EXPECTED DART CODE:")
print("=" * 60)
expected = """void main() {
    for (int i = 0; i < 5; i++) {
        print("Iteration number : $i");
    }
}"""
print(expected)

if result.strip() == expected.strip():
    print("\n✅ SUCCESS: Code matches expected output!")
else:
    print("\n❌ FAILED: Code differs from expected")