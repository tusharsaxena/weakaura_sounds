from google.cloud import texttospeech
from google.oauth2 import service_account
from pydub import AudioSegment
from pydub.playback import play

import os
import time

print (os.getcwd())

# Init parameters
OUTPUT_DIR = 'output'

# Init voice parameters
VOICE_LANGUAGE = 'en-US'
VOICE_NAME_LIST = [
    # 'en-US-Wavenet-A',
    # 'en-US-Wavenet-B',
    # 'en-US-Wavenet-C',
    # 'en-US-Wavenet-D',
    # 'en-US-Wavenet-E',
    'en-US-Wavenet-F'
]

VOLUME_LIST = [
    # 300,
    600,
    # 900,
    # 1200,
    # 1500
]

# Define text
TEXT_LIST = [
    # ('all',"gladiator's medallion"),
    # ('all','gift of the naaru'),
    # ('all','healing potion'),
    # ('all','healthstone'),
    # ('all','mana potion'),
    # ('all','shadowmeld'),
    # ('all','trinket one'),
    # ('all','trinket two'),
    # ('death knight','death grip'),
    #('death knight','death and decay'),
    #('death knight','gorefiend\'s grasp'),
    #('death knight','anti magic shell'),
    #('death knight','anti magic zone'),
    #('death knight','reaper\'s mark'),
    #('death knight','dancing rune weapon'),
    #('death knight','raise dead'),
    #('death knight','raise ally'),
    #('death knight','consumption'),
    #('death knight','blood drinker'),
    #('death knight','bone storm'),
    #('death knight','vampiric blood'),
    #('death knight','lichborne'),
    #('death knight','icebound fortitude'),
    #('death knight','tombstone'),
    #('death knight','abomination limb'),
    #('death knight','unholy assault'),
    #('death knight','dark transformation'),
    #('death knight','apocalypse'),
    #('death knight','raise abomination'),
    #('death knight','blinding sleet'),
    #('death knight','asphyxiate'),
    #('death knight','summon gargoyle'),
    # ('demon hunter','blur'),
    # ('demon hunter','chaos nova'),
    # ('demon hunter','consume magic'),
    # ('demon hunter','darkness'),
    # ('demon hunter','demon spikes'),
    # ('demon hunter','disrupt'),
    # ('demon hunter','elysian decree'),
    # ('demon hunter','essence break'),
    # ('demon hunter','eye beam'),
    # ('demon hunter','fel barrage'),
    # ('demon hunter','fel devastation'),
    # ('demon hunter','fel eruption'),
    # ('demon hunter','fel rush'),
    # ('demon hunter','felblade'),
    # ('demon hunter','fiery brand'),
    # ('demon hunter','glaive tempest'),
    # ('demon hunter','immolation aura'),
    # ('demon hunter','imprison'),
    # ('demon hunter','infernal strike'),
    # ('demon hunter','metamorphosis'),
    # ('demon hunter','netherwalk'),
    # ('demon hunter','rain from above'),
    # ('demon hunter','reverse magic'),
    # ('demon hunter','sigil of chains'),
    # ('demon hunter','sigil of flame'),
    # ('demon hunter','sigil of misery'),
    # ('demon hunter','sigil of silence'),
    # ('demon hunter','spectral sight'),
    # ('demon hunter','the hunt'),
    # ('demon hunter','throw glaive'),
    # ('demon hunter','vengeful retreat'),
    # ('druid','barkskin'),
    # ('druid','celestial alignment'),
    # ('druid','cenarion ward'),
    # ('druid','convoke the spirits'),
    # ('druid','force of nature'),
    # ('druid','grove guardians'),
    # ('druid','heart of the wild'),
    # ('druid','innervate'),
    # ('druid','ironbark'),
    # ('druid','mighty bash'),
    # ('druid','nature\'s cure'),
    # ('druid','nature\'s swiftness'),
    # ('druid','nature\'s vigil'),
    # ('druid','rebirth'),
    # ('druid','remove corruption'),
    # ('druid','solar beam'),
    # ('druid','soothe'),
    # ('druid','stampeding roar'),
    # ('druid','swiftmend'),
    # ('druid','tiger dash'),
    # ('druid','tranquility'),
    # ('druid','typhoon'),
    # ('druid','ursol\'s vortex'),
    # ('druid','wild growth'),
    # ('hunter','aspect of the cheetah'),
    # ('hunter','aspect of the turtle'),
    # ('hunter','aspect of the wild'),
    # ('hunter','bestial wrath'),
    # ('hunter','binding shot'),
    # ('hunter','camouflage'),
    # ('hunter','counter shot'),
    # ('hunter','death chakram'),
    # ('hunter','disengage'),
    # ('hunter','exhilaration'),
    # ('hunter','explosive shot'),
    # ('hunter','feign death'),
    # ('hunter','flare'),
    # ('hunter','freezing trap'),
    # ('hunter','hi explosive trap'),
    # ('hunter','intimidation'),
    # ('hunter','kill shot'),
    # ('hunter','master\'s call'),
    # ('hunter','mend pet'),
    # ('hunter','misdirection'),
    # ('hunter','primal rage'),
    # ('hunter','rapid fire'),
    # ('hunter','spirit mend'),
    # ('hunter','spirit shock'),
    # ('hunter','survival of the fittest'),
    # ('hunter','tar trap'),
    # ('hunter','tranquilizing shot'),
    # ('hunter','trueshot'),
    # ('hunter','volley'),
    # ('hunter','wailing arrow'),
    # ('mage','alter time'),
    # ('mage','arcane orb'),
    # ('mage','arcane surge'),
    # ('mage','blazing barrier'),
    # ('mage','blizzard'),    
    # ('mage','combustion'),
    # ('mage','comet storm'),
    # ('mage','counterspell'),
    # ('mage','dragon\'s breath'),
    # ('mage','evocation'),
    # ('mage','frost nova'),
    # ('mage','frozen orb'),
    # ('mage','ice block'),
    # ('mage','ice cold'),
    # ('mage','ice nova'),
    # ('mage','icy veins'),
    # ('mage','invisibility'),
    # ('mage','living bomb'),
    # ('mage','mass barrier'),
    # ('mage','meteor'),
    # ('mage','mirror image'),
    # ('mage','prismatic barrier'),
    # ('mage','ray of frost'),
    # ('mage','ring of frost'),
    # ('mage','supernova'),
    # ('mage','time warp'),
    # ('mage','touch of the magi'),
    # ('monk','chee burst'),
    # ('monk','dampen harm'),
    # ('monk','diffuse magic'),
    # ('monk','essence font'),
    # ('monk','fortifying brew'),
    # ('monk','grapple weapon'),
    # ('monk','invoke chee jee'),
    # ('monk','invoke youlawn'),
    # ('monk','invoke zuuen'),
    # ('monk','jadefire stomp'),
    # ('monk','leg sweep'),
    # ('monk','life cocoon'),
    # ('monk','paralysis'),
    # ('monk','refreshing jade wind'),
    # ('monk','revival'),
    # ('monk','ring of peace'),
    # ('monk','serenity'),
    # ('monk','spear hand strike'),
    # ('monk','storm earth and fire'),
    # ('monk','thunder focus tea'),
    # ('monk','touch of death'),
    # ('monk','touch of karma'),
    # ('monk','transcendence'),
    # ('monk','way of the crane'),
    # ('monk','whirling dragon punch'),
    # ('monk','zen focus tea'),
    # ('paladin','avenging wrath'),
    # ('paladin','blessing of freedom'),
    # ('paladin','blessing of protection'),
    # ('paladin','blessing of sacrifice'),
    # ('paladin','blinding light'),
    # ('paladin','cleanse toxins'),
    # ('paladin','divine protection'),
    # ('paladin','divine shield'),
    # ('paladin','divine steed'),
    # ('paladin','divine toll'),
    # ('paladin','execution sentence'),
    # ('paladin','final reckoning'),
    # ('paladin','hammer of justice'),
    # ('paladin','hammer of wrath'),
    # ('paladin','intercession'),
    # ('paladin','lay on hands'),
    # ('paladin','rebuke'),
    # ('paladin','shield of vengeance'),
    # ('paladin','wake of ashes'),
    # ('priest','angelic feather'),
    # ('priest','apotheosis'),
    # ('priest','circle of healing'),
    # ('priest','dark ascension'),
    # ('priest','dark ascension'),
    # ('priest','desperate prayer'),
    # ('priest','dispersion'),
    # ('priest','divine hymn'),
    # ('priest','divine star'),
    # ('priest','divine word'),
    # ('priest','fade'),
    # ('priest','guardian spirit'),
    # ('priest','halo'),
    # ('priest','holy word chastise'),
    # ('priest','holy word sanctify'),
    # ('priest','holy word serenity'),
    # ('priest','leap of faith'),
    # ('priest','mass dispel'),
    # ('priest','mind games'),
    # ('priest','mindbender'),
    # ('priest','pain suppression'),
    # ('priest','penance'),
    # ('priest','power infusion'),
    # ('priest','power word barrier'),
    # ('priest','power word life'),
    # ('priest','power word radiance'),
    # ('priest','power word shield'),
    # ('priest','prayer of mending'),
    # ('priest','psychic horror'),
    # ('priest','psychic scream'),
    # ('priest','purify'),
    # ('priest','rapture'),
    # ('priest','rapture'),
    # ('priest','shadow crash'),
    # ('priest','shadow word death'),
    # ('priest','shadowfiend'),
    # ('priest','shining force'),
    # ('priest','silence'),
    # ('priest','symbol of hope'),
    # ('priest','ultimate penitence'),
    # ('priest','vampiric embrace'),
    # ('priest','void eruption'),
    # ('priest','void torrent'),
    # ('rogue','adrenaline rush'),
    # ('rogue','between the eyes'),
    # ('rogue','blade flurry'),
    # ('rogue','blade rush'),
    # ('rogue','blind'),
    # ('rogue','cloak of shadows'),
    # ('rogue','crimson vial'),
    # ('rogue','evasion'),
    # ('rogue','gouge'),
    # ('rogue','grappling hook'),
    # ('rogue','kick'),
    # ('rogue','kidney shot'),
    # ('rogue','killing spree'),
    # ('rogue','marked for death'),
    # ('rogue','riposte'),
    # ('rogue','roll the bones'),
    # ('rogue','shadow step'),
    # ('rogue','slice and dice'),
    # ('rogue','sprint'),
    # ('rogue','toxic blade'),
    # ('rogue','vanish'),
    # ('rogue','vendetta'),
    # ('shaman','ancestral guidance'),
    # ('shaman','ascendance'),
    # ('shaman','astral shift'),
    # ('shaman','capacitor totem'),
    # ('shaman','cleanse spirit'),
    # ('shaman','cloudburst totem'),
    # ('shaman','downpour'),
    # ('shaman','earth elemental'),
    # ('shaman','earthbind totem'),
    # ('shaman','earthen wall totem'),
    # ('shaman','earthgrab totem'),
    # ('shaman','fire elemental'),
    # ('shaman','grounding totem'),
    # ('shaman','gust of wind'),
    # ('shaman','healing rain'),
    # ('shaman','healing stream totem'),
    # ('shaman','healing tide totem'),
    # ('shaman','heroism'),
    # ('shaman','hex'),
    # ('shaman','icefury'),
    # ('shaman','lightning lasso'),
    # ('shaman','liquid magma totem'),
    # ('shaman','mana tide totem'),
    # ('shaman','nature\'s swiftness'),
    # ('shaman','primordial wave'),
    ('shaman','purify spirit'),
    # ('shaman','spirit link totem'),
    # ('shaman','spirit walk'),
    # ('shaman','spirit walker\'s grace'),
    # ('shaman','stoneskin totem'),
    # ('shaman','storm elemental'),
    # ('shaman','stormkeeper'),
    # ('shaman','thunderstorm'),
    # ('shaman','tranquil air totem'),
    # ('shaman','tremor totem'),
    # ('shaman','unleash life'),
    # ('shaman','unleash shield'),
    # ('shaman','wellspring'),
    # ('shaman','wind rush totem'),
    # ('shaman','wind shear'),
    # ('warlock','cataclysm'),
    # ('warlock','channel demon fire'),
    # ('warlock','conflagrate'),
    # ('warlock','dark pact'),
    # ('warlock','demonic circle teleport'),
    # ('warlock','devour magic'),
    # ('warlock','dimensional rift'),
    # ('warlock','fel domination'),
    # ('warlock','havoc'),
    # ('warlock','malevolence'),
    # ('warlock','mortal coil'),
    # ('warlock','seduction'),
    # ('warlock','shadow bulwark'),
    # ('warlock','shadowburn'),
    # ('warlock','shadowfury'),
    # ('warlock','soulstone'),
    # ('warlock','spell lock'),
    # ('warlock','summon infernal'),
    # ('warlock','unending resolve'),
    # ('warrior','avatar'),
    # ('warrior','berserker rage'),
    # ('warrior','bitter immunity'),
    # ('warrior','demoralizing shout'),
    # ('warrior','dragon roar'),
    # ('warrior','enraged regeneration'),
    # ('warrior','heroic leap'),
    # ('warrior','impending victory'),
    # ('warrior','intimidating shout'),
    # ('warrior','last stand'),
    # ('warrior','odyn\'s fury'),
    # ('warrior','pummel'),
    # ('warrior','rallying cry'),
    # ('warrior','ravager'),
    # ('warrior','recklessness'),
    # ('warrior','shield wall'),
    # ('warrior','shockwave'),
    # ('warrior','siege breaker'),
    # ('warrior','spear of bastion'),
    # ('warrior','spell reflection'),
    # ('warrior','storm bolt'),
]

# Loop through voices
for VOICE_NAME in VOICE_NAME_LIST:

    # Instantiates a client
    credentials_filename = os.path.join(os.getcwd(),"GOOGLE_CREDENTIALS.json")
    credentials = service_account.Credentials.from_service_account_file(credentials_filename)
    client = texttospeech.TextToSpeechClient()

    # Build the voice request, select the language code ("en-US") and the ssml
    voice = texttospeech.VoiceSelectionParams(
        language_code=VOICE_LANGUAGE, name=VOICE_NAME)

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.1,
        # effects_profile_id=['large-home-entertainment-class-device'],
        # volume_gain_db=16.0
    )

    # Loop through texts
    for (classname, text) in TEXT_LIST:
        # Build file name
        filename = text.replace(' ', '_') + '.mp3'

        # Build path name for base file
        pathname = OUTPUT_DIR + '/' + VOICE_NAME + '/' + str(0) + '/' + classname.replace(' ', '_')
        if os.path.exists(pathname) == False:
            os.makedirs(pathname)

        # Set the text input to be synthesized
        synthesis_text = text + ' ready'
        synthesis_input = texttospeech.SynthesisInput(text=synthesis_text)

        # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        # Write base file 
        output_file = pathname + '/' + filename
        with open(output_file, 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file: ' + output_file)

        # Loop through volumes
        for VOLUME in VOLUME_LIST:
            
            # Build pathname for volume file
            louder_pathname = OUTPUT_DIR + '/' + VOICE_NAME + '/' + str(VOLUME) + '/' + classname.replace(' ', '_')
            if os.path.exists(louder_pathname) == False:
                os.makedirs(louder_pathname)
            
            # Write volume file
            louder_output_file = louder_pathname + '/' + filename
            song = AudioSegment.from_mp3(output_file)
            louder_song = song
            louder_song.export(louder_output_file, format='mp3', bitrate="64k", parameters=["-vol", str(VOLUME)])
            print('Audio content written to file: ' + louder_output_file)

        # Sleep for 1 second
        # time.sleep(1)
