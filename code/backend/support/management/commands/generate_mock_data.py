from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.utils.text import slugify

from support.models import Flow
from support.models import TroubleshootingLogicBlock, Tag

class Command(BaseCommand):
    help = 'Fills in mock TLBs into database'

    def handle(self, *args, **options):
        Tag.objects.all().delete()
        Flow.objects.all().delete()
        TroubleshootingLogicBlock.objects.all().delete()

        tags_restart = [Tag.objects.create(name='neustarten'),
                       Tag.objects.create(name='reboot'),
                       Tag.objects.create(name='restart'),
                       Tag.objects.create(name='resetten'),
                       Tag.objects.create(name='noi schtarte'),
                       ]

        tags_redlight = [Tag.objects.create(name='rotes Licht'),
                      Tag.objects.create(name='rotes Lämpchen blinkt'),
                      ]

        tags_wifi = [Tag.objects.create(name='wifi'),
                     Tag.objects.create(name='WLAN'),
                     Tag.objects.create(name='Wierläss'),
                     ]

        tags_fiber = [Tag.objects.create(name='fiber'),
                      Tag.objects.create(name='Glasfaser'),
                      ]

        tags_port = [Tag.objects.create(name='port'),
                      Tag.objects.create(name='port öffnen'),
                     Tag.objects.create(name='tcp'),
                     Tag.objects.create(name='udp'),
                      ]

        tags_config = [Tag.objects.create(name='Konfiguration'),
                     Tag.objects.create(name='Konfigurationsmenü'),
                     Tag.objects.create(name='Configuration'),
                     Tag.objects.create(name='10.0.0.1'),
                     ]

        tags_router = [Tag.objects.create(name='Router'),
                      Tag.objects.create(name='Rauter'),
                      Tag.objects.create(name='Modem'),
                      ]

        tlb1 = TroubleshootingLogicBlock.objects.create(
            title="Router neu starten",
            content="Um den Router neu zu starten, entfernen Sie das Stromkabel zum Router für mindestens 30 Sekunden.",
        )
        tlb1.tags.add(*(tags_restart + tags_redlight))

        tlb2 = TroubleshootingLogicBlock.objects.create(
            title="Glasfaserkabel Anschluss überprüfen",
            content="Stellen Sie sicher, dass das Glasfaserkabel korrekt mit dem Modem und der Glasfaserdose verbunden ist. Beim Einstecken des Kabels sollte ein Klickgeräusch hörbar sein.",
        )
        tlb2.tags.add(*tags_fiber)

        tlb1.successors.add(tlb2)

        tlb3 = TroubleshootingLogicBlock.objects.create(
            title="Den Router auf Werkseinstellungen zurücksetzen",
            content="Drücken Sie die Reset Taste an Ihrem Router bis die LED gelb blinkt. Warten Sie, bis die LED grün blinkt."
        )
        # NO TAGS YET
        tlb2.successors.add(tlb3)

        tlb4 = TroubleshootingLogicBlock.objects.create(
            title="Üperprüfen Sie, ob Sie den Verstand verloren haben :-)",
            content="Steht ein pinkes Einhorn in ihrem Wohnzimmer? Haben die Menschen in Ihrem Umfeld mehr als 2 Augen? Falls Sie eine dieser Fragen mit Ja beanworten, dann empfehlen wir Ihnen, unseren Support nicht zu kontaktieren.",
        )
        tlb4.tags.add(*tags_fiber)
        tlb4.successors.add()
        tlb3.successors.add(tlb4)

        tlb5 = TroubleshootingLogicBlock.objects.create(
            title="Mit dem WLAN verbinden",
            content="Auf der Unterseite Ihres Routers finden Sie den Namen Ihres WLANs (SSID) und das dazugehörige Passwort. Stellen Sie sicher, dass Sie sich mit dem korrekten WLAN verbunden haben.",
        )
        tlb5.tags.add(*tags_wifi)
        tlb5.successors.add(tlb1)

        tlb6 = TroubleshootingLogicBlock.objects.create(
            title="Auf das Konfigurationsmenü des Routers zugreifen",
            content="Um auf das Konfigurationsmenü zuzugreifen, stellen Sie sicher, dass Sie mit dem korrekten WLAN verbunden sind und rufen sie die Seite http://10.0.0.1 mit ihrem Router auf. ",
        )
        tlb6.tags.add(*tags_config)

        tlb7 = TroubleshootingLogicBlock.objects.create(
            title="Einloggen in das Konfigrationsmenü des Routers",
            content="Den korrekten Benutzernamen und das korrekte Passwort finden Sie auf der Unterseite Ihres Routers.",
        )
        tlb7.tags.add(*tags_config)
        tlb7.successors.add(tlb3)
        tlb6.successors.add(tlb7)

        tlb8 = TroubleshootingLogicBlock.objects.create(
            title="Port freigeben",
            content="Um den Port freizugeben klicken Sie auf `Einstellungen`, dann auf `Internet`, dann auf `Port freigeben`. Sie können nun den gewünschten `Port`, das `Protokoll (UDP oder TCP)` und den `Zielcomputer` auswählen. ",
        )
        tlb8.tags.add(*tags_port)
        #tlb8.successors.add()

        tlb9 = TroubleshootingLogicBlock.objects.create(
            title="Firewall deaktivieren",
            content="Um die Firewall zu deaktivieren, klicken Sie auf `Einstellungen `, dann auf `Firewall`, und dann auf `deaktivieren`. Sie müssen dies noch mit `ok` bestätigen.",
        )
        #tlb9.tags.add(tags_fiber)
        #tlb9.successors.add()

        tlb10 = TroubleshootingLogicBlock.objects.create(
            title="Kundenportal login",
            content="Besuchen Sie unsere Webseite `https://https://quickline.ch/` und klicken Sie auf `Login` oben rechts.",
        )
        #tlb10.tags.add(tags_fiber)
        #tlb10.successors.add()


        tlb11 = TroubleshootingLogicBlock.objects.create(
            title="Den Bridge Mode meines Modem/Routers aktivieren",
            content="Um den Bridge Mode des Modem/Routers zu aktivieren, klicken Sie auf `Einstellungen `, dann auf `DHCP`, und dann auf `Bridge Mode`. ",
        )
        tlb11.tags.add(*tags_config)
        #tlb11.successors.add()


        tlb12 = TroubleshootingLogicBlock.objects.create(
            title="Mein eigener Router verwenden.",
            content="Um Ihren eigenen Router zu verwenden, müssen Sie diesen erst konfigurieren und mit einem Ethernetkabel an einen `LAN` Port des Quickline Modem/Router verbinden.",
        )
        #tlb12.tags.add(tags_fiber)
        tlb12.successors.add(tlb11)
