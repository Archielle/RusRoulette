# нужен план. есть два игрока и пистолет. У игроков есть жизни и выбор в кого стрелять. У ружья есть обойма
# В обойме есть пули двух типов. Заряженная и холостая.
from random import shuffle, choice, randrange

class Player:

    def __init__(self, name, lives, hand):
        self.name = name
        self.lives = lives
        self.hand = hand

    def step(self, knife, queue_round, handcuffs):
        while len(self.hand) != 0:
            print(f'Доступные предметы: {self.hand}\n')
            player_choice = input('1 - стрелять в противника, 2 - стрелять в себя, или выбрать предмет\n')
            if player_choice in items or player_choice in cheats:
                if player_choice == 'round2':
                    queue_round = 'wait'
                    break
                if player_choice == 'showmegun':
                    print(gun)
                if player_choice == 'lens' and player_choice in self.hand:
                    self.use_glass()
                if player_choice == 'beer' and player_choice in self.hand:
                    self.use_beer()
                if player_choice == 'cigarette' and player_choice in self.hand:
                    self.use_cigarette()
                if player_choice == 'knife' and player_choice in self.hand:
                    knife = self.use_knife(knife)
                if player_choice == 'handcuffs' and player_choice in self.hand:
                    handcuffs = self.use_handcuffs(handcuffs)
            else:
                break

        if len(self.hand) == 0:
            while True:
                player_choice = input('1 - стрелять в противника, 2 - стрелять в себя\n')
                if player_choice == 'showmegun':
                    print(gun)
                elif player_choice == 'round2':
                    queue_round = 'wait'
                    break
                elif player_choice == '1' or player_choice == '2':
                    break

        return player_choice, knife, queue_round, handcuffs

    def shoot(self):
        self.lives -= 1
        print(f'у игрока "{self.name}" осталось {self.lives} жизней\n')

    def use_glass(self):
        print(translate[gun[-1]])
        self.hand.remove('lens')

    def use_beer(self):
        print(translate[gun[-1]])
        gun.pop()
        self.hand.remove('beer')

    def use_cigarette(self):
        if self.lives < 6:
            self.lives += 1
            print(f'У вас {self.lives} жизней')
            self.hand.remove('cigarette')
        else:
            print('У вас максимальное количество жизней')

    def use_knife(self, knife):
        knife = 'Yes'
        self.hand.remove('knife')
        return knife

    def use_handcuffs(self, handcuffs):
        if handcuffs == 'No':
            handcuffs = 'Yes'
            self.hand.remove('handcuffs')
            return handcuffs
        else:
            print('Вы уже использовали наручники в этом раунде')

items = ('lens', 'beer', 'cigarette', 'knife', 'handcuffs')
knife = 'No'
handcuffs = 'No'
allowed_items = 1
cartridge = ('charged', 'idle')
translate = {'charged': 'заряженная', 'idle': "холостая", 'glass': 'лупа'}
quantity = (3, 4)
run = True
gun = []
turn_step = 1
queue_round = 'round1'
cheats = ('round2', 'showmegun')

def gun_churging(queue_round, allowed_items):
    gun = ['charged', 'idle']
    round_quantity = choice(quantity)
    handcuffs = 'No'
    if queue_round == 'round2':
        if allowed_items < 6:
            allowed_items += 1
        round_quantity += randrange(4)
        for i in players:
            while len(i.hand) < allowed_items:
                i.hand.append(choice(items))
    while len(gun) < round_quantity:
        gun.append(choice(cartridge))
    print(gun)
    shuffle(gun)
    return gun, allowed_items

def change_player(turn_step):
        return 3 - turn_step

def game_step(player, opponent, turn_step, knife, queue_round, handcuffs):
    print(f'Ход игрока {player.name}')
    player_choice, knife, queue_round, handcuffs = player.step(knife, queue_round, handcuffs)

    if player_choice == '1':
        if gun[-1] == 'charged':
            print(f'Пуля оказалась {translate[gun[-1]]}\n')
            opponent.shoot()
            if knife == 'Yes':
                opponent.shoot()
                knife = 'No'
        else:
            print(f'Пуля оказалась {translate[gun[-1]]}\n')
        if handcuffs != 'Yes':
            turn_step = change_player(turn_step)
        else:
            handcuffs = "None"
    elif player_choice == '2':
        if gun[-1] == 'charged':
            print(f'Пуля оказалась {translate[gun[-1]]}\n')
            player.shoot()
            if knife == 'Yes':
                player.shoot()
                knife = 'No'
            if handcuffs != 'Yes':
                turn_step = change_player(turn_step)
            else:
                handcuffs = "None"
        else:
            print(f'Пуля оказалась {translate[gun[-1]]}\n')

    gun.pop()
    return turn_step, queue_round

player = Player('Миша', 2, [])
dealer = Player('Инна', 2, [])
players = [player, dealer]

while run:

    while queue_round in ['round1', 'round2']:

        if len(gun) == 0:
            gun, allowed_items = gun_churging(queue_round, allowed_items)
            print('Дилер мешает пули и заряжает пистолет\n')

        for i in players:
            print(f'У игрока {i.name} {i.lives} жизней')
        if turn_step == 1:
            turn_step, queue_round = game_step(player, dealer, turn_step, knife, queue_round, handcuffs)
        else:
            turn_step, queue_round = game_step(dealer, player, turn_step, knife, queue_round, handcuffs)

        if dealer.lives <= 0 or player.lives <= 0:
            if queue_round == 'round1':
                queue_round = 'wait'
            else:
                run = False
                break

    if queue_round == 'wait':
        for i in players:
            i.lives = 6
            i.hand = []
            allowed_items = 1
        gun = []
        queue_round = 'round2'
