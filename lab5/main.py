from mylib import InfoMetrics

message = "01011001100100101011010100"
poly = "1010111"
k = 26
r = 6
n = k + r

g_matrix = InfoMetrics.generate_matrix(poly, n, k)
print("Generating matrix G:")
for row in g_matrix:
    print(' '.join(map(str, row)))

canonical_g_matrix = InfoMetrics.to_canonical_form(g_matrix, n, k)
print("\nCanonical generating matrix Gk:")
for row in canonical_g_matrix:
    print(' '.join(map(str, row)))

check_matrix = InfoMetrics.generate_check_matrix(canonical_g_matrix, n, k)
print("\nCheck matrix H:")
for row in check_matrix:
    print(' '.join(map(str, row)))

canonical_check_matrix = InfoMetrics.transpose_matrix(check_matrix)
print("\nCanonical check matrix Hk:")
for row in canonical_check_matrix:
    print(' '.join(map(str, row)))

print("Message:", message)
red_bits = InfoMetrics.calculate_redundant_bits(message, canonical_check_matrix)
print("\nRedundant bits:", red_bits)

message_with_1_error = InfoMetrics.introduce_errors(message, 1)
red_bits_1_error = InfoMetrics.calculate_redundant_bits(message_with_1_error, canonical_check_matrix)
print("\nRedundant bits with 1 error:", red_bits_1_error)

corrected_word = InfoMetrics.correct_error(message_with_1_error, red_bits, canonical_check_matrix)
print("Message after error correction:", corrected_word)

message_with_2_errors = InfoMetrics.introduce_errors(message, 2)
red_bits_2_errors = InfoMetrics.calculate_redundant_bits(message_with_2_errors, canonical_check_matrix)
print("\nRedundant bits with 2 errors:", red_bits_2_errors)
corrected_word_2 = InfoMetrics.correct_error(message_with_2_errors, red_bits, canonical_check_matrix)
print("Message after error correction:", corrected_word_2)
