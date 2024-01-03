import telebot
import pokebase as pb

class Pokemon:
    def __init__(self,name):
        self.name = name
        self.api_data = pb.pokemon(name)
        try:
            self.get_id()
        except AttributeError as e:
            self.api_data = None

    def get_id(self):
        """
        It gets the pokemon's ID, wich I will use it to check 
        if the queried pokemon exist. 
        If we attempt to search for a non-existent Pokémon using PokeBase, the library 
        connected to PokeAPI, it will return an 'AttributeError', With that value, 
        I can use a 'try' statement. This way, we prevent the application 
        from closing as a result of that error.
        Returns:
            int: An integer with the Pokemon's ID
        """
        id = self.api_data.id
        return id

    def get_info(self):
        """
        It gets the detailed information about a queried pokemon
        Returns:
            str: A formatted string containing information about the Pokémon 
            including its name, attack, defense, special attack
            special defense, speed, and weight.
        """
        attack = self.api_data.stats[1].base_stat
        defense = self.api_data.stats[2].base_stat
        specialAttack = self.api_data.stats[3].base_stat
        specialDefense = self.api_data.stats[4].base_stat
        speed = self.api_data.stats[5].base_stat
        weight = self.api_data.weight
            
        return f'Estadisticas base:\n' \
               f'Nombre: {self.name}\nAtaque: {attack}\nDefensa: {defense}\n' \
               f'Ataque Especial: {specialAttack}\nDefensa Especial: {specialDefense}\n' \
               f'Velocidad: {speed}\nPeso: {weight}'
    
    def get_img(self):
        """
        it gets the queried pokemon's Sprite
        Returns:
            str: A string containing the URL of the Pokemon's sprite.
        """
        id = self.api_data.id
        img = pb.SpriteResource('pokemon',id)
        
        return img.url

#Connectivity with the bot
TOKEN = '6889333455:AAGBmOjViTSK4Rx4GY443eb5NWuwesGujTQ' #YOUR_TOKEN_HERE
bot = telebot.TeleBot(TOKEN)

#Creating chat commands
#Start Command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! Bienvenido al bot de busqueda de pokemón.\nUsa /search "nombre_del_pokemon" para buscar un pokemón por ejemplo: /search charmander')
#Help Command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Puedes interactuar conmigo usando comandos.\nUsa /start para iniciar el bot\nUsa /search "nombre_del_pokemon" para buscar un pokemón por ejemplo: /search charmander\nUsa /help para ver los comandos disponibles')
#Search Command
@bot.message_handler(commands=['search'])
def send_pokemon(message):
    pokeName = message.text.split()[1] if len(message.text.split()) > 1 else None
    if pokeName:
        queriedPokemon = Pokemon(pokeName)
        if queriedPokemon.api_data != None:
            pokeInfo = queriedPokemon.get_info()
            pokeImg = queriedPokemon.get_img()
            bot.send_photo(chat_id=message.chat.id, photo=pokeImg)
            bot.reply_to(message,pokeInfo)
        else:
            bot.reply_to(message,"Pokemon no encontrado")
    else:
        bot.reply_to(message,"Por favor proporciona el nombre del pokemon, por ejemplo: /search charmander")

#Respond to random messages
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    welcomeMessage = 'Hola bienvenido a pokebot, para inicar usa /start y si tienes dudas de como usar el bot ingresa /help'
    bot.reply_to(message,welcomeMessage)

if __name__ == "__main__":
    bot.polling(none_stop=True)
