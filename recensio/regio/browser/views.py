from recensio.plone.browser.homepage import HomepageView
from recensio.plone.browser.pdfgen import GeneratePdfRecension


class GeneratePdfRecensionRegio(GeneratePdfRecension):
    """Customized cover page"""

    logo_main = "++resource++recensio.regio.images/logo2_fuer-Deckblatt.jpg"


class RegioHomepageView(HomepageView):

    resource_directory = "++resource++recensio.regio.images"
    review_languages = [u""]
