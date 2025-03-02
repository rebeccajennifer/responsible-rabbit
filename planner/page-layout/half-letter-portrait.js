
//______________________________________________________________________
//______________________________________________________________________
//      _   __   _   _ _   _   _   _         _
// |   |_| | _  | | | V | | | | / |_/ |_| | /
// |__ | | |__| |_| |   | |_| | \ |   | | | \_
//  _  _         _ ___  _       _ ___   _                     / /
// /  | | |\ |  \   |  | / | | /   |   \                     (^^)
// \_ |_| | \| _/   |  | \ |_| \_  |  _/                     (____)o
//______________________________________________________________________
//______________________________________________________________________
//
//----------------------------------------------------------------------
// Copyright 2024, Rebecca Rashkin
// -------------------------------
// This code may be copied, redistributed, transformed, or built
// upon in any format for educational, non-commercial purposes.
//
// Please give me appropriate credit should you choose to use this
// resource. Thank you :)
//----------------------------------------------------------------------
//
//______________________________________________________________________
// //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
//______________________________________________________________________
// DESCRIPTION
// Contains code to generate two half sheets printed on one 8.5 x 11
// letter size sheet of paper. Accounts for a 1/2 left margin for
// binding
//______________________________________________________________________

//______________________________________________________________________
// CONSTANTS
//______________________________________________________________________
const letter_wdth_portrait_in  = 11;
const letter_hght_portrait_in  = 8.5;

// Standard dpi for html
const dpi                = 96;

const letter_wdth_portrait_px  = dpi * letter_wdth_portrait_in;
const letter_hght_portrait_px  = dpi * letter_hght_portrait_in;

const half_letter_wdth_portrait_px  = letter_wdth_portrait_px * 0.5;
const half_letter_hght_portrait_px  = letter_hght_portrait_px * 0.5;

//______________________________________________________________________
// Margins
//______________________________________________________________________

// To account for left binding
const std_margin_in     = 0.25;
const binder_margin_in  = 0.5;
const l_margin_in       = std_margin_in;
const r_margin_in       = std_margin_in;
const t_margin_in       = binder_margin_in;
const b_margin_in       = std_margin_in;

const l_margin_px   = l_margin_in   * dpi;
const std_margin_px = std_margin_in * dpi;
const r_margin_px   = r_margin_in   * dpi;
const t_margin_px   = t_margin_in   * dpi;
const b_margin_px   = b_margin_in   * dpi;

//______________________________________________________________________
// Content Dimensions
//______________________________________________________________________
//

const content_size_wdth_px =
  half_letter_wdth_portrait_px - l_margin_px - r_margin_px;

const content_size_hght_px =
  half_letter_hght_portrait_px - t_margin_px - b_margin_px;

// Width of middle column that serves as margin
const mid_margin_hght = t_margin_px + b_margin_px;
//______________________________________________________________________

let half_letter_layout = document.createElement("table");

half_letter_layout.style.width  = content_size_wdth_px + "px";
half_letter_layout.style.height = content_size_hght_px + "px";

const page_border_color     = "#888888";
const color                 = "#880888";
const color_page_border_style     = `1px solid ${color}`;
const page_border_style     = `1px solid ${page_border_color}`;
half_letter_layout.style.border = color_page_border_style;


function create_half_page_layout()
{
  document.getElementById("table-container").appendChild(half_letter_layout);

  let row0 = document.createElement("tr");
  let row1 = document.createElement("tr");
  let row2 = document.createElement("tr");

  let top_content          = document.createElement("td");
  top_content.style.height = content_size_hght_px + "px";

  let bottom_content          = document.createElement("td");
  bottom_content.style.height = content_size_hght_px + "px";

  let mid_margins           = document.createElement("td");
  mid_margins.style.height  = mid_margin_hght+ "px";

  half_letter_layout.style.padding  = "0px";
  top_content.style.padding         = "0px";
  bottom_content.style.padding      = "0px";
  mid_margins.style.padding         = "0px";

  top_content.style.border   = page_border_style;
  bottom_content.style.border  = page_border_style;

  row0.appendChild(top_content);
  row1.appendChild(mid_margins);
  row2.appendChild(bottom_content);

  half_letter_layout.style.borderCollapse = "collapse";
  half_letter_layout.appendChild(row0);
  half_letter_layout.appendChild(row1);
  half_letter_layout.appendChild(row2);
}

create_half_page_layout();

