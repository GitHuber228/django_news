from settings.models import SiteMainSettingsModel, SiteSocialNetModel


def get_site_mail_settings():
    return SiteMainSettingsModel.objects.first()


def get_site_social_net_list():
    return SiteSocialNetModel.objects.all()
