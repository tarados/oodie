export default function links() {
   const links = [
     {route: "/", title: "MenuHome"},
     {route: "/about", title: "MenuAboutUs"},
     {route: "/brands",
       title: "MenuBrandsFriends",
       nestedRoutes: {route: "/brands/"}
    },
     {route: "/contacts", title: "MenuContacts"}
   ];

  return links
}
