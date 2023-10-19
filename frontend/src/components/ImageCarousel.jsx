import React from "react";
import { Box, Grid, Typography } from "@mui/material";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import interview from "../assets/interview.png"
import SampleFlashCard from "./SampleFlashCard";

function ImageCarousel() {
    return (
      <Carousel showThumbs={false} infiniteLoop={true} autoPlay={false} interval={3000}>
        <div>
          <img src={interview} alt="Interview 1" />
        </div>
        <div>
          {/* <img src={interview} alt="Interview 2" /> */}
          <SampleFlashCard />
        </div>
        <div>
          <img src={interview} alt="Interview 3" />
        </div>
      </Carousel>
    );
  };

  export default ImageCarousel;