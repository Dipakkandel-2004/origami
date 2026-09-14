# Tourist-facing map areas shown on the home page map. This is a curated set
# of ~20 popular tourist areas (not all 47 prefectures, and not just the 8
# broad regions) — the level of detail a travel agency's visitors actually
# look for.
#
# Each area:
#   - key:          unique slug for this area
#   - label:         name shown on hover
#   - region:         parent region, used for color grouping (see the
#                     dest-map-region--<region> classes in _home_map.html)
#   - match_names:    names tried in order against Destination.name
#                     (case-insensitive "contains") to find which Destination
#                     record this area should link to. First match wins.
#   - path:           the SVG <path> "d" attribute for this area's shape,
#                     against viewBox 0 0 420 920 in _home_map.html.
TOURIST_AREAS = [
    {
        "key": "hokkaido", "label": "Hokkaido", "region": "hokkaido",
        "match_names": ["Hokkaido", "Sapporo"],
        "path": "M300,20 L350,55 L335,120 L285,128 L250,85 Z",
    },
    {
        "key": "aomori", "label": "Aomori", "region": "tohoku",
        "match_names": ["Aomori"],
        "path": "M250,130 L310,140 L300,182 L240,185 L222,158 Z",
    },
    {
        "key": "sendai", "label": "Sendai", "region": "tohoku",
        "match_names": ["Sendai", "Miyagi", "Matsushima"],
        "path": "M240,185 L300,182 L298,225 L240,232 L218,178 Z",
    },
    {
        "key": "tokyo", "label": "Tokyo", "region": "kanto",
        "match_names": ["Tokyo"],
        "path": "M275,232 L328,238 L320,270 L268,278 L258,268 Z",
    },
    {
        "key": "yokohama", "label": "Yokohama", "region": "kanto",
        "match_names": ["Yokohama", "Kanagawa"],
        "path": "M268,278 L320,270 L322,298 L272,304 Z",
    },
    {
        "key": "kanazawa", "label": "Kanazawa", "region": "chubu",
        "match_names": ["Kanazawa", "Ishikawa"],
        "path": "M175,225 L250,230 L240,258 L170,260 Z",
    },
    {
        "key": "fuji", "label": "Mt. Fuji", "region": "chubu",
        "match_names": ["Fuji", "Hakone", "Yamanashi"],
        "path": "M170,260 L240,258 L232,292 L165,295 Z",
    },
    {
        "key": "nagoya", "label": "Nagoya", "region": "chubu",
        "match_names": ["Nagoya", "Aichi"],
        "path": "M165,295 L232,292 L225,325 L160,328 Z",
    },
    {
        "key": "kyoto", "label": "Kyoto", "region": "kansai",
        "match_names": ["Kyoto"],
        "path": "M172,330 L232,326 L226,362 L168,365 Z",
    },
    {
        "key": "osaka", "label": "Osaka", "region": "kansai",
        "match_names": ["Osaka"],
        "path": "M168,365 L226,362 L220,400 L165,404 Z",
    },
    {
        "key": "nara", "label": "Nara", "region": "kansai",
        "match_names": ["Nara"],
        "path": "M220,362 L235,360 L230,405 L222,400 Z",
    },
    {
        "key": "kobe", "label": "Kobe", "region": "kansai",
        "match_names": ["Kobe", "Hyogo"],
        "path": "M145,360 L168,365 L165,404 L150,408 Z",
    },
    {
        "key": "hiroshima", "label": "Hiroshima", "region": "chugoku",
        "match_names": ["Hiroshima", "Miyajima"],
        "path": "M60,330 L110,332 L100,398 L55,400 L35,360 Z",
    },
    {
        "key": "okayama", "label": "Okayama", "region": "chugoku",
        "match_names": ["Okayama"],
        "path": "M110,332 L155,335 L140,395 L100,398 Z",
    },
    {
        "key": "takamatsu", "label": "Takamatsu", "region": "shikoku",
        "match_names": ["Takamatsu", "Kagawa"],
        "path": "M185,407 L215,405 L205,455 L180,458 Z",
    },
    {
        "key": "matsuyama", "label": "Matsuyama", "region": "shikoku",
        "match_names": ["Matsuyama", "Ehime"],
        "path": "M150,410 L185,407 L180,458 L155,460 Z",
    },
    {
        "key": "fukuoka", "label": "Fukuoka", "region": "kyushu",
        "match_names": ["Fukuoka"],
        "path": "M40,410 L120,415 L112,450 L48,452 Z",
    },
    {
        "key": "nagasaki", "label": "Nagasaki", "region": "kyushu",
        "match_names": ["Nagasaki"],
        "path": "M10,460 L48,452 L45,490 L15,495 Z",
    },
    {
        "key": "kumamoto", "label": "Kumamoto", "region": "kyushu",
        "match_names": ["Kumamoto"],
        "path": "M48,452 L112,450 L105,485 L52,487 Z",
    },
    {
        "key": "kagoshima", "label": "Kagoshima", "region": "kyushu",
        "match_names": ["Kagoshima"],
        "path": "M45,490 L105,485 L105,510 L30,515 Z",
    },
    {
        "key": "okinawa", "label": "Okinawa", "region": "okinawa",
        "match_names": ["Okinawa"],
        "path": "M55,690 L90,685 L95,715 L60,720 Z",
    },
]


def get_map_areas():
    """Resolve each tourist area to a Destination, when one exists.

    Returns a list of dicts (one per TOURIST_AREAS entry) with an added
    "destination" key: the matching active Destination if found, else None.
    Matching tries each of the area's match_names, in order, as a
    case-insensitive "contains" match against Destination.name.
    """
    from .models import Destination

    areas = []
    for area in TOURIST_AREAS:
        destination = None
        for term in area["match_names"]:
            destination = Destination.objects.filter(
                is_active=True, name__icontains=term
            ).first()
            if destination:
                break
        areas.append({**area, "destination": destination})
    return areas