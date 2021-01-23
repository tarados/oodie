import store from '../store'

export default function localizeFilter(key, defaultValue) {
  if (!key && defaultValue) {
    return defaultValue;
  }
  let defaultLocale = window.navigator.language || 'ua-UA';
  const locale = store.getters.getLocale || defaultLocale;
  const locales = store.getters.getLocales;
  if (locales && locales[locale] && locales[locale][key]) {
    return locales[locale][key];
  }
  return key;
}