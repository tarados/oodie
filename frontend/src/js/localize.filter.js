import store from '../store'

export default function localizeFilter(key) {
  try {
    const locale = store.getters.getLocale || 'ru-RU'
    const locales = store.getters.getLocales
    return locales[locale][key] || `key ${key} not found`
  } catch (TypeError) {
    return `key ${key} not found`
    // location.reload();
  }

}