
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
// TODO
//______________________________________________________________________
// half-letter-portrait and half-letter-landscape have a lot of
// duplicate code - these should be refactored to eliminate
// duplication.
//______________________________________________________________________

//______________________________________________________________________
// CONSTANTS
//______________________________________________________________________
// Note: This file uses constants from an external file. The html that
// calls this script should first list the constants file before
// listing this file.
//______________________________________________________________________
const letter_wdth_portrait_in  = 8.5;
const letter_hght_portrait_in  = 11;

const letter_wdth_portrait_px  = DPI * letter_wdth_portrait_in;
const letter_hght_portrait_px  = DPI * letter_hght_portrait_in;

// Container for left and right content tables
// Table the entire size of a sheet
let half_letter_layout = document.createElement("table");
half_letter_layout.style.width   = letter_wdth_portrait_px + "px";
half_letter_layout.style.height  = letter_hght_portrait_px + "px";
half_letter_layout.style.border  = CONTENT_BORDER_STYLE;
half_letter_layout.style.margin  = 0;

//document.getElementById("table-container")
//  .appendChild(half_letter_layout);

//______________________________________________________________________
// Margins
//______________________________________________________________________

// To account for left binding
const std_margin_in     = 0.25;
const binder_margin_in  = 0.5;

const l_margin_in       = std_margin_in;
const r_margin_in       = std_margin_in;
const b_margin_in       = std_margin_in;

let t_margin_in       = 0;

// Change margin sides depending on double-sided print
if (DOUBLE_SIDED)
{
  t_margin_in       = std_margin_in;
}
else
{
  t_margin_in       = binder_margin_in;
}

// Convert in to px
const std_margin_px     = std_margin_in     * DPI;
const binder_margin_px  = binder_margin_in  * DPI;

const l_margin_px = l_margin_in * DPI;
const r_margin_px = r_margin_in * DPI;
const t_margin_px = t_margin_in * DPI;
const b_margin_px = b_margin_in * DPI;


//______________________________________________________________________
// Content Dimensions
//______________________________________________________________________

// Full width of half sheet with no margins
const half_letter_wdth_portrait_px  = letter_wdth_portrait_px;

// Content size (with margins)
const content_size_wdth_px =
  half_letter_wdth_portrait_px - l_margin_px - r_margin_px;

// Width of middle column that serves as margin
// Will account for two binder margins if printing double sided
// Otherwise will assume
let mid_margin_hght = 0;

if (DOUBLE_SIDED)
{
  mid_margin_hght = 2 * binder_margin_px;
}
else
{
  mid_margin_hght = t_margin_px + b_margin_px;
}

// Height of
const content_size_hght_px =
  0.5 * (letter_hght_portrait_px - mid_margin_hght);

//______________________________________________________________________
/*
let row0 = document.createElement("tr");
let row1 = document.createElement("tr");
let row2 = document.createElement("tr");

let top_content           = document.createElement("td");
top_content.style.height  = content_size_hght_px + "px";
let top_content_container = document.createElement("div");

top_content_container.style.border  = CONTENT_BORDER_STYLE;
top_content_container.style.width   =
  content_size_wdth_px - CONTENT_PADDING + "px";
top_content.appendChild(top_content_container);

let bottom_content          = document.createElement("td");
bottom_content.style.height = content_size_hght_px + "px";
bottom_content.style.padding = "10px";
let bot_content_container = document.createElement("div");
//bot_content_container.border.style = CONTENT_BORDER_STYLE;
//bottom_content.appendChild(bot_content_container);

let mid_margins           = document.createElement("td");
mid_margins.style.height  = mid_margin_hght + "px";

//half_letter_layout.style.paddingTop     = t_margin_px + "px";
//half_letter_layout.style.paddingBottom  = b_margin_px + "px";
//half_letter_layout.style.paddingLeft    = l_margin_px + "px";
//half_letter_layout.style.paddingRight   = r_margin_px + "px";

top_content.style.padding         = "0px";
bottom_content.style.padding      = "0px";
mid_margins.style.padding         = "0px";

top_content.style.border    = CONTENT_BORDER_STYLE;
bottom_content.style.border = CONTENT_BORDER_STYLE;

row0.appendChild(top_content);
row1.appendChild(mid_margins);
row2.appendChild(bottom_content);

//half_letter_layout.style.borderCollapse = "collapse";
half_letter_layout.appendChild(row0);
half_letter_layout.appendChild(row1);
half_letter_layout.appendChild(row2);
*/

let letter_size_div = document.createElement("div");
letter_size_div.style.width   = letter_wdth_portrait_px + "px";
letter_size_div.style.height  = letter_hght_portrait_px + "px";
letter_size_div.style.border  = DEBUG_BORDER_STYLE;
letter_size_div.style.padding = CONTENT_PADDING;
letter_size_div.style.padding = CONTENT_PADDING;

document.getElementById("table-container")
  .appendChild(letter_size_div);

page_wdth = half_letter_wdth_portrait_px + "px";

let top_content_box = document.createElement("div");
top_content_box.style.height  = content_size_hght_px + "px";
top_content_box.style.width   = page_wdth;
top_content_box.style.border  = DEBUG_BORDER_STYLE;

let mid_margin_box = document.createElement("div");
mid_margin_box.style.height = mid_margin_hght + "px";
mid_margin_box.style.width  = page_wdth;
mid_margin_box.style.border  = DEBUG_BORDER_STYLE;

let bot_content_box = document.createElement("div");
bot_content_box.style.height  = content_size_hght_px  + "px";
bot_content_box.style.width   = page_wdth;
bot_content_box.style.border  = DEBUG_BORDER_STYLE;


letter_size_div.appendChild(top_content_box);
letter_size_div.appendChild(mid_margin_box);
letter_size_div.appendChild(bot_content_box);