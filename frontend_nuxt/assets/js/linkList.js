export default function links() {
   const links = [
     {route: "/", title: "MenuHome"},
     {route: "/about", title: "MenuAboutUs"},
     {route: "/brands", title: "MenuBrandsFriends", nestedRoutes: [
        {route: "/some-route-1", title: "SomeRoute1"},
        {route: "/some-route-1", title: "SomeRoute2"},
    ]},
     {route: "/contacts", title: "MenuContacts"}
   ];

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
