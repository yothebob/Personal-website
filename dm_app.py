import dm_data as dd
import random

class Dm_App():


    def gen_name(self):
            choice = random.randrange(1,5)
            if choice == 1:
                name = random.choice(dd.prefix) + random.choice(dd.middle) + random.choice(dd.suffix)
            elif choice == 2:
                name = random.choice(dd.prefix) + random.choice(dd.suffix)
            elif choice == 3:
                name = random.choice(dd.prefix) + random.choice(dd.middle)
            elif choice == 4:
                name = random.choice(dd.middle) + random.choice(dd.suffix)
            return name

    def gen_menu(self,_num):
        print()
        genmenu=[(random.choice(dd.food) + ', ' + random.choice(dd.drink)) for x in range(_num)]
        return genmenu

    def gen_npc(self):
        npc = []
        npc.append('Name: ' + self.gen_name())
        npc.append('Appearance: ' + random.choice(dd.appearance))
        npc.append('Race: ' + random.choice(dd.race))
        npc.append('Gender: ' + random.choice(dd.gender))
        npc.append('Skill: ' + random.choice(dd.skilled))
        npc.append('Talent: ' + random.choice(dd.talent))
        npc.append('Mannerism: ' + random.choice(dd.mannerism))
        npc.append('Ideals: ' + random.choice(dd.ideals))
        npc.append('Flaw: ' + random.choice(dd.flaw))
        return npc

    def gen_tavern_event(self,_num):
        res = [random.choice(dd.tavern_events) for x in range(_num)]
        return res

    def gen_tavern(self):
        tav_dict = {}
        gen_begin = random.choice(dd.description)
        gen_mid = random.choice(dd.animal)
        gen_end = random.choice(dd.end)
        choose = random.randrange(1,4)
        tav_trait = random.choice(dd.tavern_traits)
        menu = self.gen_menu(4)
        staff = [random.choice(dd.prefix)+ random.choice(dd.middle)+ random.choice(dd.suffix) for x in range(random.randrange(1,5))]
        staff_traits = ''
        event = self.gen_tavern_event(random.randrange(1,4))
        if tav_trait == 'secret monster/s hiding ':
            tav_trait = tav_trait + random.choice(dd.monsters)
        if tav_trait == 'completely run by ':
            tav_trait = tav_trait + random.choice(dd.monsters)
        if tav_trait == 'everyone inside gets a magic cantrip ability':
            tav_trait = tav_trait + random.choice(dd.magic)
        tav_dict['trait'] = tav_trait
        tav_dict['menu'] = menu
        tav_dict['event'] = event
        tav_dict['staff'] = staff
        tav_dict['owner'] = self.gen_npc()
        if choose == 1:
            tavern = ('The ' + gen_begin + gen_end)
        elif choose == 2:
            tavern = ('The ' + gen_begin + gen_mid)
        else:
            tavern = ('The ' + gen_begin + gen_mid + gen_end)
        tav_dict['name'] = tavern
        return tav_dict

    def roll_dice(self,dice_type,rolls):
        total = 0
        for roll in range(rolls):
            roll = random.randrange(1,(dice_type + 1))
            total += roll
        return total

    def gen_city(self,city_size,city_num=1):
        city_dict = {}
        taverns_dict = {}
        if city_size.lower() == 's':
            total_inns = 1
            shops = 4
        elif city_size.lower() == 'm':
            total_inns = 2
            shops = 6
        elif city_size.lower() == 'l':
            total_inns = 3
            shops = 10
        city_dict['reason']=random.choice(dd.city_reason)
        for num in range(city_num):
            for bar in range(total_inns):
                tavern = self.gen_tavern()
                barkeep = self.gen_npc()
                taverns_dict[tavern['name']] = tavern
            stores = self.gen_shops(shops)
            city_dict['taverns'] = taverns_dict
            city_dict['stores'] = stores
        return city_dict


    def gen_shops(self,_num):
        shop_dict = {}
        for store in range(_num):
            name = random.choice(dd.shop)
            shop_dict[name] = []
            owner = self.gen_npc()
            shop_dict[name].append(owner)
        return shop_dict

    def gen_idea(self,_num):
        ideas = [(random.choice(dd.pronoun) + random.choice(dd.verb)+ random.choice(dd.noun)) for x in range(_num)]
        return ideas

    def gen_poi(self,_num):
        pois = [random.choice(dd.locations) for x in range(_num)]
        return pois

    def gen_hook(self,_num):
        hooks = [random.choice(dd.plot_hook) for x in range(_num)]
        return hooks
