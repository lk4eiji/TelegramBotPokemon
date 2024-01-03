import telebot
import pokebase as pb

class Pokemon:
    def __init__(self,name):
        self.name = name
        self.api_data = pb.pokemon(name)

    def get_info(self):
        """
        Obtene la información del pokemon
        Returns:
            str: información del pokemon
        """
        attack = self.api_data.stats[1].base_stat
        deffense = self.api_data.stats[2].base_stat
        specialAttack = self.api_data.stats[3].base_stat
        specialDeffense = self.api_data.stats[4].base_stat
        speed = self.api_data.stats[5].base_stat
        weight = self.api_data
            
        
        return f'Estadisticas base:\n' \
               f'Nombre: {self.name}\nAtaque: {attack}\nDefensa:{deffense}' \
               f'Ataque Especial: {specialAttack}\nDefensa Especial: {specialDeffense}' \
               f'Velocidad: {speed}\nPeso: {weight}'
    
#Get pokemon's ID
def get_pokemonId(pokemonName):
    if pokemonName:
        pokemon = pb.pokemon(pokemonName)
        pokeId = pokemon.id
        return pokeId
    else:
        return 'Pokemon no encontrado'

#Get Pokemon's Sprite
def get_pokemonImg(pokemonId):
    if pokemonId:
        pokeImg = pb.SpriteResource('pokemon',pokemonId)
        return pokeImg.url
    else:
        return 'Pokemon no encontrado'

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
        pokeId = get_pokemonId(pokeName)
        pokeInfo = get_pokemon(pokeName)
        pokeImg = get_pokemonImg(pokeId)
        bot.send_photo(chat_id=message.chat.id, photo=pokeImg)
        bot.reply_to(message,pokeInfo)
    else:
        bot.reply_to(message,"Por favor proporciona el nombre del pokemon, por ejemplo: /search charmander")

#Respond to random messages
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    welcomeMessage = 'Hola bienvenido a pokebot, para inicar usa /start y si tienes dudas de como usar el bot ingresa /help'
    bot.reply_to(message,welcomeMessage)

if __name__ == "__main__":
    bot.polling(none_stop=True)
