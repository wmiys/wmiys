<!doctype html>
<html lang="en">

<head>
    <?php include('header.php'); ?>
    <title>Create a new product</title>
</head>

<body>
    <?php include('navbar.php'); ?>

    <div class="container pb-3">

        <!-- <h1 class="text-center mt-5">New Product</h1> -->

        <form class="form-new-product mt-5">

            <ul class="nav nav-pills nav-fill form-new-product-tabs d-none" id="myTab" role="tablist">
                <li class="nav-item" role="presentation">
                    <a class="nav-link active" data-toggle="tab" href="#form-new-product-page-category" role="tab">Category</a>
                </li>
                <li class="nav-item" role="presentation">
                    <a class="nav-link " data-toggle="tab" href="#form-new-product-page-location" role="tab">Location</a>
                </li>
                <li class="nav-item" role="presentation">
                    <a class="nav-link" data-toggle="tab" href="#form-new-product-page-renter-info" role="tab">Renter Info</a>
                </li>
                <li class="nav-item" role="presentation">
                    <a class="nav-link" data-toggle="tab" href="#form-new-product-page-photos" role="tab">Photos</a>
                </li>
                <li class="nav-item" role="presentation">
                    <a class="nav-link" data-toggle="tab" href="#form-new-product-page-name-desc" role="tab">Name and Description</a>
                </li>
                <li class="nav-item" role="presentation">
                    <a class="nav-link" data-toggle="tab" href="#form-new-product-page-price" role="tab">Price</a>
                </li>
            </ul>

            <div class="progress mb-5">
                <div class="progress-bar bg-secondary" role="progressbar" style="width: 17%;"></div>
            </div>

            <p class="subtitle text-primary mb-3">ADD NEW PRODUCT</p>

            <div class="tab-content form-new-product-pages">
                <!-- category -->
                <div class="tab-pane show active" id="form-new-product-page-category">
                    <!-- panel heading -->
                    <div class="d-flex flex-column flex-md-row justify-content-md-between">
                        <h2>Categories</h2>
                        <h2 class="text-muted">Step 1</h2>
                    </div>
                    <hr>

                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Category</h4>
                            <p class="text-muted text-sm">Select a category that best describes your product. This will help renters find and book your listing.</p>
                        </div>

                        <div class="col-lg-8">
                            <!-- major -->
                            <div class="form-group mb-4">
                                <label for="form-new-product-input-category-major">Major</label>
                                <select class="form-control form-new-product-input" id="form-new-product-input-category-major" required>
                                </select>
                                <div class="invalid-feedback">Invalid feedback text</div>
                            </div>

                            <!-- minor -->
                            <div class="form-group mb-4">
                                <label for="form-new-product-input-category-minor">Minor</label>
                                <select class="form-control form-new-product-input" id="form-new-product-input-category-minor" required disabled>
                                </select>
                                <div class="invalid-feedback">Invalid feedback text</div>
                            </div>

                            <!-- sub -->
                            <div class="form-group mb-3">
                                <label for="form-new-product-input-category-sub">Sub</label>
                                <select class="form-control form-new-product-input" id="form-new-product-input-category-sub" required disabled>
                                </select>
                                <div class="invalid-feedback">Invalid feedback text</div>
                            </div>
                        </div>
                    </div>

                    <hr>
                    <div class="form-new-product-step-btns d-flex justify-content-between">
                        <button type="button" data-page-location="1" class="btn btn-text-light form-new-product-btn-step mr-2" disabled><i class='bx bx-arrow-back'></i> Previous</button>
                        <button type="button" data-page-location="2" class="btn btn-text-primary form-new-product-btn-step">Next <i class='bx bx-right-arrow-alt'></i></button>
                    </div>
                </div>

                <!-- location -->
                <div class="tab-pane" id="form-new-product-page-location">
                    <div class="d-flex flex-column flex-md-row justify-content-md-between">
                        <h2>Location</h2>
                        <h2 class="text-muted">Step 2</h2>
                    </div>
                    <hr>

                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Pick up location</h4>
                            <p class="text-muted text-sm">Where should renters pick up your product?</p>
                        </div>

                        <div class="col-lg-8">
                            <div class="form-group">
                                <label for="form-new-product-input-location">City and state</label>
                                <div class="input-group input-group-search">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text" id="basic-addon1"><i class='bx bx-search'></i></span>
                                    </div>
                                    <select class="form-control form-new-product-input" id="form-new-product-input-location" required placeholder="Search"></select>
                                </div>

                                <div class="invalid-feedback">Invalid feedback text</div>
                                <p class="text-muted mt-2"><small>The exact address won’t be shared until the guest’s reservation is confirmed.</small></p>
                            </div>
                        </div>
                    </div>
                    <hr>

                    <div class="form-new-product-step-btns d-flex justify-content-between">
                        <button type="button" data-page-location="1" class="btn btn-text-light form-new-product-btn-step mr-2"><i class='bx bx-arrow-back'></i> Previous</button>
                        <button type="button" data-page-location="3" class="btn btn-text-primary form-new-product-btn-step">Next <i class='bx bx-right-arrow-alt'></i></button>
                    </div>
                </div>

                <!-- Renter Info -->
                <div class="tab-pane" id="form-new-product-page-renter-info">
                    <!-- panel heading -->
                    <div class="d-flex flex-column flex-md-row justify-content-md-between">
                        <h2>Requirements</h2>
                        <h2 class="text-muted">Step 3</h2>
                    </div>
                    <hr>

                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Who can rent your product?</h4>
                            <p class="text-muted text-sm">Keep in mind that someone booking your experience might book spots for other guests. If there are strict requirements around age, skill level, or certifications, include them here.</p>
                        </div>

                        <div class="col-lg-8">
                            <p>Placeholder for all the shit we are going to display to the lender about the renters requirements. Airbnb has some optional requirements like: minimum age, verified government id, text box for additional requirements.</p>
                        </div>
                    </div>
                    <hr>

                    <div class="form-new-product-step-btns d-flex justify-content-between">
                        <button type="button" data-page-location="2" class="btn btn-text-light form-new-product-btn-step mr-2"><i class='bx bx-arrow-back'></i> Previous</button>
                        <button type="button" data-page-location="4" class="btn btn-text-primary form-new-product-btn-step">Next <i class='bx bx-right-arrow-alt'></i></button>
                    </div>
                </div>


                <!-- photos -->
                <div class="tab-pane" id="form-new-product-page-photos">
                    <!-- panel heading -->
                    <div class="d-flex flex-column flex-md-row justify-content-md-between">
                        <h2>Photos</h2>
                        <h2 class="text-muted">Step 4</h2>
                    </div>
                    <hr>

                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Cover photo</h4>
                            <p class="text-muted text-sm">Your main product photo.</p>
                        </div>
                        <div class="col-lg-8">
                            <div class="form-group">
                                <div class="custom-file">
                                    <input type="file" class="custom-file-input form-new-product-input" id="form-new-product-input-photos">
                                    <label class="custom-file-label" for="form-new-product-input-photos">Choose photo</label>
                                </div>
                                <p class="text-muted mt-2"><small>If you don't have a photo available, you can always add or change it later.</small></p>
                                <div class="invalid-feedback">Invalid feedback text</div>
                            </div>
                        </div>
                    </div>
                    <hr>

                    <p>We can put tips and advice here for selecting good, quality photos.</p>
                    <hr>

                    <div class="form-new-product-step-btns d-flex justify-content-between">
                        <button type="button" data-page-location="3" class="btn btn-text-light form-new-product-btn-step mr-2"><i class='bx bx-arrow-back'></i> Previous</button>
                        <button type="button" data-page-location="5" class="btn btn-text-primary form-new-product-btn-step">Next <i class='bx bx-right-arrow-alt'></i></button>
                    </div>
                </div>

                <!-- name and description -->
                <div class="tab-pane" id="form-new-product-page-name-desc">
                    <!-- panel heading -->
                    <div class="d-flex flex-column flex-md-row justify-content-md-between">
                        <h2>Texts</h2>
                        <h2 class="text-muted">Step 5</h2>
                    </div>
                    <hr>

                    <!-- name -->
                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Name</h4>
                            <p class="text-muted text-sm">Give your product a name</p>
                        </div>

                        <div class="col-lg-8">
                            <div class="form-group">
                                <label for="form-new-product-input-name">What is the name of your product?</label>
                                <input class="form-control form-new-product-input" id="form-new-product-input-name" type="text" required>
                                <div class="invalid-feedback">Invalid feedback text</div>
                                <p class="text-muted mt-2"><small>Make it short, descriptive, and exciting.</small></p>
                            </div>
                        </div>
                    </div>

                    <hr>

                    <!-- description -->
                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Description</h4>
                            <p class="text-muted text-sm">Your product description is a chance to inspire renters to reserve your listing.</p>
                        </div>

                        <div class="col-lg-8">
                            <div class="form-group">
                                <label for="form-new-product-input-description">Describe your product to renters</label>
                                <textarea class="form-control form-new-product-input" id="form-new-product-input-description" rows="7" required></textarea>
                                <div class="invalid-feedback">Invalid feedback text</div>
                            </div>
                        </div>
                    </div>

                    <hr>

                    <div class="form-new-product-step-btns d-flex justify-content-between">
                        <button type="button" data-page-location="4" class="btn btn-text-light form-new-product-btn-step mr-2"><i class='bx bx-arrow-back'></i> Previous</button>
                        <button type="button" data-page-location="6" class="btn btn-text-primary form-new-product-btn-step">Next <i class='bx bx-right-arrow-alt'></i></button>
                    </div>

                </div>

                <!-- price -->
                <div class="tab-pane" id="form-new-product-page-price">

                    <div class="d-flex flex-column flex-md-row justify-content-md-between">
                        <h2>Pricing</h2>
                        <h2 class="text-muted">Step 6</h2>
                    </div>
                    <hr>

                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Full day</h4>
                            <p class="text-muted text-sm">Total price for a full day.</p>
                        </div>

                        <div class="col-lg-8">

                            <!-- full day price -->
                            <div class="form-group">
                                <label for="form-new-product-input-price-full">How much to rent for the day?</label>
                                <div class="input-group">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">$</span>
                                    </div>
                                    <input class="form-control form-new-product-input" id="form-new-product-input-price-full" type="text" inputmode="decimal" required>
                                </div>
                                <div class="invalid-feedback">Invalid feedback text</div>
                                <p class="text-muted mt-2"><small></small></p>
                            </div>


                        </div>
                    </div>
                    <hr>

                    <!-- half day price -->
                    <div class="row mt-5">
                        <div class="col-lg-4">
                            <h4>Half day</h4>
                            <p class="text-muted text-sm">Total price for a half day.</p>
                        </div>

                        <div class="col-lg-8">
                            <div class="form-group">
                                <label for="form-new-product-input-price-half">How much to rent for half the day?</label>
                                <div class="input-group">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">$</span>
                                    </div>
                                    <input inputmode="decimal" class="form-control form-new-product-input" id="form-new-product-input-price-half" type="text" required>
                                </div>
                                <div class="invalid-feedback">Invalid feedback text</div>
                            </div>
                        </div>
                    </div>
                    <hr>

                    <div class="form-new-product-step-btns d-flex justify-content-between">
                        <button type="button" data-page-location="5" class="btn btn-text-light form-new-product-btn-step mr-2"><i class='bx bx-arrow-back'></i> Previous</button>
                        <button type="button" class="btn btn-primary form-new-product-btn-submit">Finish</button>
                    </div>

                </div>
            </div>
        </form>
    </div>


    <?php include('footer.php'); ?>
    <script src="js/create-product.js"></script>

</body>

</html>