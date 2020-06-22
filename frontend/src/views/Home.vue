<template>
  <div>
    <Navbar/>
    <Hamburger/>
    <header class="showcase">
      <div class="container showcase-inner">
        <h1>Winter Sale Now On!</h1>
        <p>One size fits all hooded blanket perfect for those chilly mornings and cold afternoons!</p>
        <a href="#" class="btn">BUY NOW</a>
      </div>
    </header>
    <ProductsList thumbnail="large"/>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";
    import Hamburger from "../components/Hamburger"
    import ProductsList from "../components/ProductsList";

    export default {
        name: 'Home',
        components: {
            Navbar,
            Hamburger,
            ProductsList
        }
    }
</script>

<style>
  /*section one - header*****************************************************************************/
  .container {
    max-width: 960px;
    margin: auto;
    overflow: hidden;
    padding: 0.3rem;
  }

  .showcase {
    content: '';
    background: url("../assets/tile.jpg") no-repeat center center/cover;
    width: 100%;
    height: 650px;
  }

  .showcase .showcase-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    height: 100%;
  }

  .showcase h1 {
    font-size: 2.5rem;
  }

  .showcase p {
    font-size: 1.2rem;
  }

  .btn {
    display: inline-block;
    font-family: "montreal-serialbold", sans-serif;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    white-space: normal;
    font-size: 14px;
    border: none;
    border-radius: 3px;
    background-color: white;
    color: black;
    padding: 0.75rem 1.5rem;
    margin-top: 1rem;
    text-decoration: none;
    transition: opacity 1s ease-in;
  }

  .btn:hover {
    opacity: 0.7;
  }

  /*section two -  collections oodie******************************************************************/
  .collections {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
  }

  .wrapper_collections {
    padding: 55px;
  }

  .item_collections {
    flex: 0 1 50%;
  }

  .item_collections_image_wrapper {
    max-width: 436px;
    max-height: 545px;
    margin: 0 auto 19px;
    position: relative;
    width: 100%;
  }

  .item_collections_image {
    max-width: 436px;
    max-height: 545px;
  }

  /*media queries********************************************************************************************/

  @media screen and (min-width: 1200px) {

  }

  @media screen and (max-width: 750px) {
    .showcase {
      height: 490px;
    }
  }

  @media screen and (max-width: 420px) {

  }

  @media screen and (max-width: 375px) {
    .logo svg {
      width: 34vw;
    }
  }

  @media screen and (max-width: 360px) {
    .logo svg {
      width: 34vw;
    }
  }


</style>
