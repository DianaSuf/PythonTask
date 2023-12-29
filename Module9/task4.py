# Частотный анализ
def filter_participants(file_name, k):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    k = int(lines[0])
    participants = []
    for line in lines[1:]:
        last_name, first_name, score = line.split()
        score = int(score)
        if score > k:
            participants.append((last_name, first_name[0], score))
    participants.sort(key=lambda x: x[2], reverse=True)
    return participants

def write_participants(file_name, participants):
    with open(file_name, 'w') as f:
        f.write(str(len(participants)) + '\n')
        for i, participant in enumerate(participants):
            last_name, first_initial, score = participant
            f.write(f"{i+1}) {first_initial}. {last_name} {score}\n")

participants = filter_participants('first_tour.txt', 80)
write_participants('second_tour.txt', participants)