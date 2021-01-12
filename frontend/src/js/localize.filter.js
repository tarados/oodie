import store from '../store'

export default function localizeFilter(key) {
  const locale = store.getters.getLocale || 'ru-RU'
  const locales = store.getters.getLocales
  return locales[locale][key] || `key ${key} not found`
}