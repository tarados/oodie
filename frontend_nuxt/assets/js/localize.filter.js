import store from '../store'

export default function localizeFilter(key, defaultValue) {
  if (!key && defaultValue) {
    return defaultValue;
  }

  const locale = store.state.locale;
  const locales = store.state.locales;
  if (locales && locales[locale] && locales[locale][key]) {
    return locales[locale][key];
  }
  return key;
}
