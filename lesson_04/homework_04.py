adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.
"""

# task 01
# Замініть символ переносу рядка на пробіл
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02
# Замініть .... на пробіл
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03
# Зробіть так, щоб у тексті був лише один пробіл між словами
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())

# task 04
# Порахуйте, скільки разів зустрічається літера "h"
print("Кількість літер 'h':", adwentures_of_tom_sawer.count("h"))

# task 05
# Порахуйте кількість слів, що починаються з великої літери
words = adwentures_of_tom_sawer.split()
capital_words_count = sum(1 for word in words if word[0].isupper())
print("Кількість слів з великої літери:", capital_words_count)

# task 06
# Знайдіть позицію другого входження слова "Tom"
first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1)
print("Позиція другого входження 'Tom':", second_index)

# task 07
# Розділіть текст на речення
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
# Виведіть четверте речення у нижньому регістрі
print("Четверте речення (lowercase):")
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
# Перевірте, чи є речення, яке починається з "By the time"
starts_with_by_the_time = any(
    sentence.startswith("By the time")
    for sentence in adwentures_of_tom_sawer_sentences
)
print("Чи є речення, що починається з 'By the time':", starts_with_by_the_time)

# task 10
# Порахуйте кількість слів в останньому реченні
last_sentence_words_count = len(adwentures_of_tom_sawer_sentences[-1].split())
print("Кількість слів в останньому реченні:", last_sentence_words_count)

