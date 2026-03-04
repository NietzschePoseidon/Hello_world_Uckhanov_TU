print(f"=== Анализ последовательности ДНК ===\n")

def nucleotide_count():

    sequence = input("Введите последовательность ДНК: ").upper()

    print(f"\nПоследовательность в верхнем регистре: {sequence}")

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    len_sequence = len(sequence)
    a_procent = a_count / len_sequence
    t_procent = t_count / len_sequence
    g_procent = g_count / len_sequence
    c_procent = c_count / len_sequence

    return a_count, t_count, g_count, c_count, len_sequence, a_procent, t_procent, g_procent, c_procent

result = nucleotide_count()

print(f"\nПодсчёт нуклеотидов:\nA:\t{result[0]}\nT:\t{result[1]}\nG:\t{result[2]}\nC:\t{result[3]}")
print(f"\nОбщая длина: {result[4]}")
print(f"\nПроцентное содержание нуклеотидов:\nA:\t{result[5]:.2f}\nT:\t{result[6]:.2f}\nG:\t{result[7]:.2f}\nC:\t{result[8]:.2f}")
