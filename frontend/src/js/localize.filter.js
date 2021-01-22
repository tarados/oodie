import store from '../store'

export default function localizeFilter(key) {
  try {
    let defaultLocale = window.navigator.language || 'ua-UA'
    const locale = store.getters.getLocale || defaultLocale
    const locales = store.getters.getLocales
    return locales[locale][key] || `${key}`
  } catch (TypeError) {
    return `key ${key} not found`
    // location.reload();
  }

}