import store from '../store'


export default function titleFilter(key) {
  if (key !== null) {
    return key
  } else {
    const products = store.getters.allProducts
    products.forEach(product => {
      if (product.title_translate === null) {
        return product.title
      }
    })
  }
}