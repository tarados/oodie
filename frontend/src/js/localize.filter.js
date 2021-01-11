import store from '../store'

const locales = {
  'ru-RU': {
    'InfoTitle': 'Один размер',
    'MenuHome': 'главная'
  },
  'en-US': {
    'InfoTitle': 'One size',
    'MenuHome': 'Home'
  },
  'ua-UA': {
    'InfoTitle': 'Один розмір',
    'MenuHome': 'Головна'
  }
}

export default function localizeFilter(key) {
  const locale = store.getters.getLocale || 'ru-RU'
  return locales[locale][key] || `[Localize error]: key ${key} not found`
}