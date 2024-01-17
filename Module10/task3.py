# Регистрация
def validate_data(name, email, age):
    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if '@' not in email or '.' not in email:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")
    if not 10 <= int(age) <= 99:
        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")

def process_registrations():
    with open('registrations.txt', 'r', encoding='utf-8') as file, \
         open('registrations_good.log', 'w', encoding='utf-8') as good_log, \
         open('registrations_bad.log', 'w', encoding='utf-8') as bad_log:
        for line in file:
            try:
                name, email, age = line.strip().split()
                validate_data(name, email, age)
                good_log.write(line)
            except (IndexError, NameError, SyntaxError, ValueError) as e:
                bad_log.write(f'{line.strip()}        {str(e)}\n')

process_registrations()