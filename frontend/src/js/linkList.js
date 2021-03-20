export default function links() {
  /** TODO
   const list = [
     {route: "/", title: "MenuHome"},
     {route: "/about", title: "MenuAboutUs"},
     {route: "/brands", title: "MenuBrandsFriends", nestedRoutes: [
        {route: "/some-route-1", title: "SomeRoute1"},
        {route: "/some-route-1", title: "SomeRoute2"},
    ]},
   ];
   */

  const links = {
    '1': 'MenuHome',
    '2': 'MenuAboutUs',
    '3': 'MenuBrandsFriends',
    '4': 'MenuContacts'
  }
  return links
}

export function langList() {
  const lang = [
    {
      'title': 'RU',
      'name': 'ru-RU',
      'slug': 'ru'
    },
    {
      'title': 'UA',
      'name': 'ua-UA',
      'slug': 'ua'
    }
  ]
  return lang
}
