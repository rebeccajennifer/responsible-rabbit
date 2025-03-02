//______________________________________________________________________
//______________________________________________________________________
//      _   __   _   _ _   _   _   _         _
// |   |_| | _  | | | V | | | | / |_/ |_| | /
// |__ | | |__| |_| |   | |_| | \ |   | | | \_
//  _  _         _ ___  _       _ ___   _                    / /
// /  | | |\ |  \   |  | / | | /   |   \                    (^^)
// \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
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
// Contains code to generate landscape blank month calendar.
//______________________________________________________________________


//______________________________________________________________________
// Style Constants
//______________________________________________________________________
// Height and width have been selected to account for pages being
// printed 1/2 size with a left margin for  hole punches.
//
// Whole page:      1056 x 816, 96 DPI
// Assume margins:  Left: 1 in (96 px)
//                  Top / Bottom / Right: .5 (24 px)
//______________________________________________________________________
const page_width            = "672px";
const page_height           = "960px";
const page_border_color     = "#888888";
const page_border_style     = `1px solid ${page_border_color}`;
//______________________________________________________________________

const calendar_border_color = "#444444";
const calendar_border_style = `2px solid ${calendar_border_color}`;
const calendar_width        = "100%"
const calendar_height       = "100%"

const day_border_style = `1px solid ${calendar_border_color}`;

const date_box_width        = "25px";
const date_box_height       = "25px";
const date_box_border_style = `1px solid ${calendar_border_color}`;

//______________________________________________________________________
let page_layout = document.createElement("table");
let month_table = document.createElement("table");

//______________________________________________________________________
// Constants
//______________________________________________________________________
const day_count  = 7;
const week_count = 4;

//______________________________________________________________________
// Set styles for page and month styles
//______________________________________________________________________
function set_table_styles()
{
  page_layout.style.width   = page_width;
  page_layout.style.height  = page_height;
  page_layout.style.border  = page_border_style;
  document.getElementById("table-container").appendChild(page_layout);

  month_table.style.width  = calendar_width;
  month_table.style.height = calendar_height;
  month_table.style.border = calendar_border_style;

  const style = document.createElement("style");
  style.innerHTML =
  `
    .month-table td
    {
      border  : ${day_border_style};
      vertical-align : top;

    }

    .letter-size td
    {
      width  : auto;
      height : auto;
    }
  `;
  document.head.appendChild(style);

  month_table.classList.add("month-table");
  page_layout.classList.add("letter-size");
}

//______________________________________________________________________
// Create date box
//______________________________________________________________________
function create_date_box()
{
  let date_box    = document.createElement("div");

  date_box.style.border = date_box_border_style;
  date_box.style.width  = date_box_width;
  date_box.style.height = date_box_height;

  date_box.style.position = "absolute";
  date_box.style.top      = "0";
  date_box.style.right    = "0";

  return date_box;
}

//______________________________________________________________________
// Create 4 week calendar
//______________________________________________________________________
function create_month_calendar(rows, cols)
{
  set_table_styles();

  let row  = document.createElement("tr");
  let cell = document.createElement("td");

  cell.appendChild(month_table);
  row.appendChild(cell);
  page_layout.appendChild(row);

  for (let i = 0; i < rows; i++)
  {
    let row = document.createElement("tr");

    for (let j = 0; j < cols; j++) {
      let cell = document.createElement("td");
      cell.style.position = "relative";
      cell.appendChild(create_date_box());
      row.appendChild(cell);
    }

    let day_label = document.createElement("td");
    day_label.style.width = '30px';
    row.appendChild(day_label);

    month_table.appendChild(row);
  }
}


create_month_calendar(7, 4);
