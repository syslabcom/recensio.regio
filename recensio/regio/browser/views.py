from recensio.theme.browser.homepage import HomepageView
from recensio.theme.browser.pdfgen import GeneratePdfRecension


class GeneratePdfRecensionRegio(GeneratePdfRecension):
    """Customized cover page
    """

    logo_main = "++resource++recensio.regio.images/logo2_fuer-Deckblatt.jpg"


class RegioHomepageView(HomepageView):

    review_languages = [u""]
