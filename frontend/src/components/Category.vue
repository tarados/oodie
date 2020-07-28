<template>
  <div class="wrapper">
    <div class="container-flex">
      <div class="item header">
        Дружеские бренды
      </div>
      <div class="item categories">
        <div class="category-item">
          Boots
        </div>
        <div class="category-item">
          Trackies
        </div>
        <div class="category-item">
          Slippers
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Category"
    }
</script>

<style scoped>
  .wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1%;
  }

  .container-flex {
    margin-top: 1%;
    height: 2rem;
    display: flex;
    flex-wrap: wrap;
  }

  .item {
    flex-grow: 1;
  }

  .header {
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 600;
    font-size: 1.4375em;
    align-self: center;
  }

  .categories {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
  }

  .category-item {
    background-color: white;
    font-size: 1rem;
    padding: 2%;
  }

  .category-item:hover {
    background: #e8bd67;
    border-radius: 3rem;
    cursor: pointer;
    font-size: 1rem;
  }

  /*media queries*****************************************/
  @media screen and (max-width: 960px) {
    .header {
      font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
      text-align: center;
      margin: 5% auto;
    }

    .category-item {
      font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
    }
  }

  @media screen and (max-width: 750px) {

  }

  @media screen and (max-width: 650px) {

  }

  @media screen and (max-width: 420px) {
    .container-flex {
      display: block;
    }

    .categories {
      justify-content: space-around;
    }
  }

  @media screen and (max-width: 320px) {

  }
</style>