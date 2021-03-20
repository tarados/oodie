import store from '../store'

export default function localizeFilter(key, defaultValue) {
  if (!key && defaultValue) {
    return defaultValue;
  }

  const locale = store.getters.getLocale;
  const locales = store.getters.getLocales;
  if (locales && locales[locale] && locales[locale][key]) {
    return locales[locale][key];
  }
  return key;
}
